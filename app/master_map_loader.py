import re
from pathlib import Path
from typing import Any

from case_validator import validate_case


MASTER_MAP_FILE = Path("profiles/MASTER_MAP_DIFY_v1.0.md")


def load_master_map_text() -> str:
    if not MASTER_MAP_FILE.exists():
        raise FileNotFoundError(
            f"Không tìm thấy file MASTER_MAP: {MASTER_MAP_FILE}"
        )

    return MASTER_MAP_FILE.read_text(encoding="utf-8")


def get_section(block: str, section_name: str) -> str:
    pattern = (
        rf"## {re.escape(section_name)}\s*\n"
        rf"(.*?)(?=\n## |\n-{{10,}}|\Z)"
    )

    match = re.search(pattern, block, flags=re.DOTALL)

    if not match:
        return ""

    return match.group(1).strip()


def parse_bullet_items(section_text: str) -> list[str]:
    items: list[str] = []
    current_item = ""

    for raw_line in section_text.splitlines():
        line = raw_line.strip()

        if not line:
            continue

        if line.startswith("-"):
            if current_item:
                items.append(current_item.strip())

            current_item = line.lstrip("-").strip()
        else:
            current_item += " " + line

    if current_item:
        items.append(current_item.strip())

    return items


def parse_required_masters(
    section_text: str,
) -> list[dict[str, Any]]:
    masters: list[dict[str, Any]] = []

    for item in parse_bullet_items(section_text):
        match = re.search(
            r"(MASTER_\d+)\s*---\s*(.*?)\s*---\s*(.*)",
            item,
        )

        if match:
            masters.append(
                {
                    "master_code": match.group(1).strip(),
                    "master_name": match.group(2).strip(),
                    "requirement": match.group(3).strip(),
                }
            )
            continue

        code_match = re.search(r"(MASTER_\d+)", item)

        if code_match:
            masters.append(
                {
                    "master_code": code_match.group(1),
                    "master_name": item,
                    "requirement": "",
                }
            )

    return masters


def parse_generation_order(section_text: str) -> list[str]:
    return re.findall(r"MASTER_\d+", section_text)


def parse_case(block: str) -> dict[str, Any]:
    case_match = re.search(r"# Case:\s*(CASE_\d+)", block)

    if not case_match:
        raise ValueError("Không tìm thấy Case ID.")

    return {
        "case_id": case_match.group(1),
        "case_name": get_section(block, "Case Name"),
        "description": get_section(block, "Description"),
        "company_types": parse_bullet_items(
            get_section(block, "Company Types")
        ),
        "required_inputs": parse_bullet_items(
            get_section(block, "Required Inputs")
        ),
        "required_masters": parse_required_masters(
            get_section(block, "Required Masters")
        ),
        "generation_order": parse_generation_order(
            get_section(block, "Generation Order")
        ),
        "master_dependencies": parse_bullet_items(
            get_section(block, "Master Dependencies")
        ),
        "required_canonical_fields": parse_bullet_items(
            get_section(block, "Required Canonical Fields")
        ),
        "validation": parse_bullet_items(
            get_section(block, "Validation")
        ),
        "notes": get_section(block, "Notes"),
    }


def load_cases() -> list[dict[str, Any]]:
    text = load_master_map_text()

    blocks = re.split(
        r"(?=^# Case:\s*CASE_\d+)",
        text,
        flags=re.MULTILINE,
    )

    cases: list[dict[str, Any]] = []

    for block in blocks:
        if not block.strip().startswith("# Case:"):
            continue

        cases.append(parse_case(block))

    return cases


def main() -> None:
    cases = load_cases()

    print(f"Đã đọc {len(cases)} case.")
    print("=" * 70)

    for case in cases[:3]:
        print(f"Case ID: {case['case_id']}")
        print(f"Tên case: {case['case_name']}")
        print(f"Loại hình: {case['company_types']}")
        print("Master bắt buộc:")

        for master in case["required_masters"]:
            print(
                f"- {master['master_code']} | "
                f"{master['master_name']}"
            )

        print(f"Thứ tự tạo: {case['generation_order']}")
        print(
            "Canonical fields: "
            f"{case['required_canonical_fields']}"
        )

        warnings = validate_case(case)

        if warnings:
            print("CẢNH BÁO:")

            for warning in warnings:
                print(f"- {warning}")
        else:
            print("Không có cảnh báo.")

        print("-" * 70)


if __name__ == "__main__":
    main()