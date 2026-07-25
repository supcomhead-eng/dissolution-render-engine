from pathlib import Path
from typing import Any

from docx import Document

from app.decision_loader import (
    DECISION_PACKET_FILE,
    load_decision_packet,
)
from app.placeholder_mapping_loader import load_placeholder_mapping
from app.placeholder_scanner import scan_document
from app.replacement_builder import build_replacements
from app.word_renderer import render_document


MASTER_FOLDER = Path("masters")
OUTPUT_FOLDER = Path("output")


def validate_rendered_file(
    output_file: Path,
    mapping: dict[str, dict[str, Any]],
) -> list[str]:
    document = Document(output_file)
    remaining = sorted(scan_document(document))

    must_review: list[str] = []

    for placeholder in remaining:
        item = mapping.get(placeholder, {})
        source_type = str(item.get("source_type", "")).upper()
        notes = str(item.get("notes", "")).lower()

        allowed_to_remain = (
            source_type == "CONSTANT"
            and (
                "không replace" in notes
                or placeholder.startswith("[BEGIN_")
                or placeholder.startswith("[END_")
            )
        )

        if not allowed_to_remain:
            must_review.append(placeholder)

    return must_review


def get_selected_masters(
    packet: dict[str, Any],
) -> list[dict[str, Any]]:
    selected_masters = packet.get("selected_masters", [])

    if not isinstance(selected_masters, list):
        raise ValueError(
            "selected_masters phải là một danh sách."
        )

    if not selected_masters:
        raise ValueError(
            "Decision Packet chưa có selected_masters."
        )

    return selected_masters


def main() -> None:
    print("=" * 70)
    print("DISSOLUTION RENDER ENGINE")
    print("=" * 70)

    packet = load_decision_packet(
        DECISION_PACKET_FILE
    )

    mapping = load_placeholder_mapping()

    replacements, unresolved = build_replacements(
        packet,
        mapping,
    )

    selected_masters = get_selected_masters(packet)

    OUTPUT_FOLDER.mkdir(exist_ok=True)

    generated_files: list[Path] = []
    errors: list[str] = []
    review_report: dict[str, list[str]] = {}

    for master in selected_masters:
        master_name = str(
            master.get("master_name", "")
        ).strip()

        if not master_name:
            errors.append(
                "Có master không có master_name."
            )
            continue

        master_file = MASTER_FOLDER / master_name

        if not master_file.exists():
            errors.append(
                f"Không tìm thấy master: {master_name}"
            )
            continue

        output_file = (
            OUTPUT_FOLDER
            / f"RENDERED_{master_file.name}"
        )

        try:
            render_document(
                master_file,
                output_file,
                replacements,
            )

            generated_files.append(output_file)

            remaining = validate_rendered_file(
                output_file,
                mapping,
            )

            review_report[output_file.name] = remaining

        except Exception as error:
            errors.append(
                f"{master_name}: {error}"
            )

    print()
    print(f"Số nội dung thay thế: {len(replacements)}")
    print(
        f"Số field chưa có dữ liệu toàn hệ thống: "
        f"{len(unresolved)}"
    )
    print(f"Số file đã tạo: {len(generated_files)}")
    print("=" * 70)

    for output_file in generated_files:
        remaining = review_report.get(
            output_file.name,
            [],
        )

        print(f"FILE: {output_file.name}")

        if remaining:
            print("Trạng thái: CẦN KIỂM TRA")

            for placeholder in remaining:
                print(f"- {placeholder}")
        else:
            print("Trạng thái: SẴN SÀNG")

        print("-" * 70)

    if errors:
        print("LỖI:")

        for error in errors:
            print(f"- {error}")

        print("=" * 70)

    if generated_files and not errors:
        print("KẾT QUẢ: RENDER HOÀN TẤT.")
    else:
        print("KẾT QUẢ: CẦN KIỂM TRA LỖI.")


if __name__ == "__main__":
    main()