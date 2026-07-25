import re
from pathlib import Path
from typing import Any


PLACEHOLDER_MAPPING_FILE = Path(
    "profiles/PLACEHOLDER_MAPPING_DIFY_v0.1.md"
)


def load_placeholder_mapping_text() -> str:
    if not PLACEHOLDER_MAPPING_FILE.exists():
        raise FileNotFoundError(
            f"Không tìm thấy file: {PLACEHOLDER_MAPPING_FILE}"
        )

    return PLACEHOLDER_MAPPING_FILE.read_text(
        encoding="utf-8"
    )


def get_field(block: str, title: str) -> str:
    pattern = (
        rf"## {re.escape(title)}\s*\n"
        rf"(.*?)(?=\n## |\n\*\*\*|\Z)"
    )

    match = re.search(
        pattern,
        block,
        flags=re.DOTALL,
    )

    if not match:
        return ""

    return match.group(1).strip()


def parse_used_in_masters(text: str) -> list[str]:
    masters = []

    for line in text.splitlines():

        line = line.strip()

        if line.startswith("-"):
            masters.append(
                line.lstrip("-").strip()
            )

    return masters


def parse_placeholder(block: str) -> dict[str, Any]:

    placeholder_match = re.search(
        r"# Placeholder:\s*(\[.*?\])",
        block,
    )

    if not placeholder_match:
        raise ValueError(
            "Không tìm thấy Placeholder."
        )

    return {
        "placeholder":
            placeholder_match.group(1),

        "canonical_field":
            get_field(block, "Canonical Field"),

        "description":
            get_field(block, "Description"),

        "used_in_masters":
            parse_used_in_masters(
                get_field(
                    block,
                    "Used In Masters",
                )
            ),

        "source_type":
            get_field(
                block,
                "Source Type",
            ),

        "confidence":
            get_field(
                block,
                "Confidence",
            ),

        "reason":
            get_field(
                block,
                "Reason",
            ),

        "notes":
            get_field(
                block,
                "Notes",
            ),
    }


def load_placeholder_mapping():

    text = load_placeholder_mapping_text()

    blocks = re.split(
        r"(?=^# Placeholder:)",
        text,
        flags=re.MULTILINE,
    )

    mapping = {}

    for block in blocks:

        if not block.strip().startswith(
            "# Placeholder:"
        ):
            continue

        item = parse_placeholder(block)

        mapping[
            item["placeholder"]
        ] = item

    return mapping


def main():

    mapping = load_placeholder_mapping()

    print(
        f"Đã đọc {len(mapping)} placeholder."
    )

    print("=" * 70)

    count = 0

    for placeholder, item in mapping.items():

        print(
            f"Placeholder : {placeholder}"
        )

        print(
            f"Canonical   : {item['canonical_field']}"
        )

        print(
            f"Source      : {item['source_type']}"
        )

        print(
            f"Confidence  : {item['confidence']}"
        )

        print(
            f"Số master   : "
            f"{len(item['used_in_masters'])}"
        )

        print("-" * 70)

        count += 1

        if count >= 10:
            break


if __name__ == "__main__":
    main()