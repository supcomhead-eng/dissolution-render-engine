from pathlib import Path

from docx import Document
from app.placeholder_mapping_loader import load_placeholder_mapping
from app.placeholder_scanner import scan_document


OUTPUT_FOLDER = Path("output")


def main() -> None:
    output_files = sorted(
        OUTPUT_FOLDER.glob("RENDERED_*.docx"),
        key=lambda path: path.stat().st_mtime,
        reverse=True,
    )

    if not output_files:
        print("Không tìm thấy file RENDERED trong thư mục output.")
        return

    output_file = output_files[0]
    document = Document(output_file)

    remaining = sorted(scan_document(document))
    mapping = load_placeholder_mapping()

    must_review: list[str] = []
    intentionally_kept: list[str] = []

    for placeholder in remaining:
        item = mapping.get(placeholder, {})
        source_type = str(item.get("source_type", "")).upper()
        notes = str(item.get("notes", "")).lower()

        if (
            source_type == "CONSTANT"
            and (
                "không replace" in notes
                or placeholder.startswith("[BEGIN_")
                or placeholder.startswith("[END_")
            )
        ):
            intentionally_kept.append(placeholder)
        else:
            must_review.append(placeholder)

    print(f"FILE KIỂM TRA: {output_file.name}")
    print("=" * 70)

    print(f"Placeholder cần kiểm tra: {len(must_review)}")

    for placeholder in must_review:
        item = mapping.get(placeholder, {})

        print(
            f"- {placeholder}"
            f" | {item.get('canonical_field', 'UNKNOWN')}"
            f" | {item.get('source_type', 'UNKNOWN')}"
        )

    print("=" * 70)
    print(
        f"Placeholder được phép giữ nguyên: "
        f"{len(intentionally_kept)}"
    )

    for placeholder in intentionally_kept:
        print(f"- {placeholder}")

    if not must_review:
        print("=" * 70)
        print("KẾT QUẢ: FILE ĐÃ SẴN SÀNG.")
    else:
        print("=" * 70)
        print("KẾT QUẢ: FILE CẦN BỔ SUNG DỮ LIỆU.")


if __name__ == "__main__":
    main()