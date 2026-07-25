from typing import Any

from app.decision_loader import (
    DECISION_PACKET_FILE,
    load_decision_packet,
)
from app.placeholder_mapping_loader import load_placeholder_mapping
from app.system_resolver import resolve_system_value


SKIP_SOURCE_TYPES = {
    "CONSTANT",
}

SKIP_PLACEHOLDERS_PREFIXES = (
    "[BEGIN_",
    "[END_",
)


def extract_value(raw_value: Any) -> str | None:
    if raw_value is None:
        return None

    if isinstance(raw_value, dict):
        value = raw_value.get("normalized_value")

        if value is None:
            value = raw_value.get("value")

        if value is None:
            return None

        return str(value)

    if isinstance(raw_value, (list, tuple, set)):
        return ", ".join(str(item) for item in raw_value)

    return str(raw_value)


def build_data_pool(packet: dict[str, Any]) -> dict[str, Any]:
    data_pool: dict[str, Any] = {}

    canonical_data = packet.get("canonical_data", {})

    if isinstance(canonical_data, dict):
        data_pool.update(canonical_data)

    authorized_person = packet.get("authorized_person", {})

    if isinstance(authorized_person, dict):
        for key, value in authorized_person.items():
            canonical_key = (
                key
                if key.startswith("authorized_person_")
                else f"authorized_person_{key}"
            )

            data_pool.setdefault(canonical_key, value)

    case_summary = packet.get("case_summary", {})

    if isinstance(case_summary, dict):
        for key, value in case_summary.items():
            data_pool.setdefault(key, value)

    return data_pool


def build_replacements(
    packet: dict[str, Any],
    mapping: dict[str, dict[str, Any]],
) -> tuple[dict[str, str], list[dict[str, str]]]:
    data_pool = build_data_pool(packet)

    replacements: dict[str, str] = {}
    unresolved: list[dict[str, str]] = []

    for placeholder, item in mapping.items():
        canonical_field = str(
            item.get("canonical_field", "")
        ).strip()

        source_type = str(
            item.get("source_type", "")
        ).strip().upper()

        if source_type in SKIP_SOURCE_TYPES:
            continue

        if placeholder.startswith(SKIP_PLACEHOLDERS_PREFIXES):
            continue

        if not canonical_field or canonical_field == "UNKNOWN":
            unresolved.append(
                {
                    "placeholder": placeholder,
                    "canonical_field": canonical_field or "UNKNOWN",
                    "reason": "Không có canonical field hợp lệ.",
                }
            )
            continue

        value = extract_value(
            data_pool.get(canonical_field)
        )

        if (
            (value is None or value == "")
            and source_type == "SYSTEM"
        ):
            value = resolve_system_value(
                canonical_field
            )

        if value is None or value == "":
            unresolved.append(
                {
                    "placeholder": placeholder,
                    "canonical_field": canonical_field,
                    "reason": (
                        f"Chưa có giá trị cho Source Type "
                        f"{source_type or 'UNKNOWN'}."
                    ),
                }
            )
            continue

        replacements[placeholder] = value

    return replacements, unresolved


def main() -> None:
    packet = load_decision_packet(
        DECISION_PACKET_FILE
    )

    mapping = load_placeholder_mapping()

    replacements, unresolved = build_replacements(
        packet,
        mapping,
    )

    print(
        f"Đã tạo {len(replacements)} "
        f"nội dung thay thế."
    )
    print("=" * 70)

    for placeholder, value in list(
        replacements.items()
    )[:30]:
        print(f"{placeholder} -> {value}")

    print("=" * 70)
    print(
        f"Chưa xử lý được: "
        f"{len(unresolved)} placeholder"
    )

    for item in unresolved[:20]:
        print(
            f"- {item['placeholder']} "
            f"-> {item['canonical_field']} "
            f"| {item['reason']}"
        )


if __name__ == "__main__":
    main()