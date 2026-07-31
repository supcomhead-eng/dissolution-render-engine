from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.main import validate_rendered_file
from app.placeholder_mapping_loader import load_placeholder_mapping
from app.replacement_builder import build_replacements
from app.word_renderer import (
    get_master_file,
    render_document,
)


OUTPUT_FOLDER = Path("output")

app = FastAPI(
    title="Dissolution Render Engine",
    version="1.0",
)


class DecisionPacket(BaseModel):
    model_config = {
        "extra": "allow",
    }


@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "dissolution-render-engine",
    }


@app.post("/render")
def render(
    packet: DecisionPacket,
) -> dict[str, Any]:
    packet_data = packet.model_dump()

    selected_masters = packet_data.get(
        "selected_masters",
        [],
    )

    if (
        not isinstance(selected_masters, list)
        or not selected_masters
    ):
        raise HTTPException(
            status_code=400,
            detail=(
                "Decision Packet chưa có "
                "selected_masters."
            ),
        )

    mapping = load_placeholder_mapping()

    replacements, unresolved = build_replacements(
        packet_data,
        mapping,
    )

    OUTPUT_FOLDER.mkdir(
        parents=True,
        exist_ok=True,
    )

    generated_documents: list[
        dict[str, Any]
    ] = []

    errors: list[str] = []

    for master in selected_masters:
        if not isinstance(master, dict):
            errors.append(
                "Có phần tử trong selected_masters "
                "không phải object."
            )
            continue

        master_name = str(
            master.get("master_name", "")
        ).strip()

        if not master_name:
            errors.append(
                "Có master không có master_name."
            )
            continue

        try:
            master_file = get_master_file(
                master_name
            )

            output_file = (
                OUTPUT_FOLDER
                / f"RENDERED_{master_file.name}"
            )

            render_document(
                master_file,
                output_file,
                replacements,
            )

            remaining = validate_rendered_file(
                output_file,
                mapping,
            )

            generated_documents.append(
                {
                    "master_name": master_file.name,
                    "output_file": str(
                        output_file.resolve()
                    ),
                    "status": (
                        "ready"
                        if not remaining
                        else "needs_review"
                    ),
                    "remaining_placeholders": (
                        remaining
                    ),
                }
            )

        except Exception as error:
            errors.append(
                f"{master_name}: {error}"
            )

    if generated_documents and not errors:
        status = "success"
    elif generated_documents and errors:
        status = "partial_success"
    else:
        status = "failed"

    return {
        "status": status,
        "generated_documents": (
            generated_documents
        ),
        "unresolved_system_fields": unresolved,
        "errors": errors,
    }