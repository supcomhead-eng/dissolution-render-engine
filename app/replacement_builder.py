from typing import Any

from app.authorized_profile_loader import (
    find_authorized_profile,
)
from app.decision_loader import (
    DECISION_PACKET_FILE,
    load_decision_packet,
)
from app.placeholder_mapping_loader import (
    load_placeholder_mapping,
)
from app.system_resolver import resolve_system_value
from app.derived_field_resolver import (
    resolve_derived_value,
)


SKIP_SOURCE_TYPES = {
    "CONSTANT",
}

SKIP_PLACEHOLDERS_PREFIXES = (
    "[BEGIN_",
    "[END_",
)


def extract_value(
    raw_value: Any,
) -> str | None:
    if raw_value is None:
        return None

    if isinstance(raw_value, dict):
        value = raw_value.get(
            "normalized_value"
        )

        if value is None:
            value = raw_value.get("value")

        if value is None:
            return None

        return str(value)

    if isinstance(
        raw_value,
        (list, tuple, set),
    ):
        return ", ".join(
            str(item)
            for item in raw_value
        )

    return str(raw_value)


def build_data_pool(
    packet: dict[str, Any],
) -> dict[str, Any]:
    data_pool: dict[str, Any] = {}

    canonical_data = packet.get(
        "canonical_data",
        {},
    )

    if isinstance(canonical_data, dict):
        data_pool.update(canonical_data)

    authorized_person = packet.get(
        "authorized_person",
        {},
    )

    if isinstance(authorized_person, dict):
        requested_name = (
            authorized_person.get("name")
            or authorized_person.get(
                "authorized_person_name"
            )
            or ""
        )

        requested_name = str(
            requested_name
        ).strip()

        if requested_name:
            try:
                profile = find_authorized_profile(
                    requested_name
                )

                for key, value in profile.items():
                    if key == "aliases":
                        continue

                    data_pool.setdefault(
                        key,
                        value,
                    )

            except (
                FileNotFoundError,
                ValueError,
            ) as error:
                data_pool[
                    "_authorized_profile_lookup_error"
                ] = str(error)

        for key, value in authorized_person.items():
            canonical_key = (
                key
                if key.startswith(
                    "authorized_person_"
                )
                else f"authorized_person_{key}"
            )

            data_pool.setdefault(
                canonical_key,
                value,
            )

    case_summary = packet.get(
        "case_summary",
        {},
    )

    if isinstance(case_summary, dict):
        for key, value in case_summary.items():
            data_pool.setdefault(
                key,
                value,
            )

    return data_pool


def build_replacements(
    packet: dict[str, Any],
    mapping: dict[str, dict[str, Any]],
) -> tuple[
    dict[str, str],
    list[dict[str, str]],
]:
    data_pool = build_data_pool(packet)

    # determine master context (conservative: use first selected master name if any)
    selected_masters = packet.get("selected_masters", []) or []
    master_name = None
    if isinstance(selected_masters, list) and selected_masters:
        first = selected_masters[0]
        if isinstance(first, dict):
            master_name = first.get("master_name")

    profile_lookup_error = extract_value(
        data_pool.pop(
            "_authorized_profile_lookup_error",
            None,
        )
    )

    replacements: dict[str, str] = {}

    unresolved: list[
        dict[str, str]
    ] = []

    if profile_lookup_error:
        unresolved.append(
            {
                "placeholder": (
                    "[HỒ SƠ NGƯỜI ĐƯỢC ỦY QUYỀN]"
                ),
                "canonical_field": (
                    "authorized_person_profile"
                ),
                "reason": profile_lookup_error,
            }
        )

    for placeholder, item in mapping.items():
        canonical_field = str(
            item.get(
                "canonical_field",
                "",
            )
        ).strip()

        source_type = str(
            item.get(
                "source_type",
                "",
            )
        ).strip().upper()

        if source_type in SKIP_SOURCE_TYPES:
            continue

        if placeholder.startswith(
            SKIP_PLACEHOLDERS_PREFIXES
        ):
            continue

        if (
            not canonical_field
            or canonical_field == "UNKNOWN"
        ):
            unresolved.append(
                {
                    "placeholder": placeholder,
                    "canonical_field": (
                        canonical_field
                        or "UNKNOWN"
                    ),
                    "reason": (
                        "Không có canonical "
                        "field hợp lệ."
                    ),
                }
            )
            continue

        # 1. try direct canonical field from data_pool
        value = extract_value(
            data_pool.get(
                canonical_field
            )
        )

        # 2. if missing, attempt derived/alias resolution
        if (value is None or value == ""):
            try:
                derived = resolve_derived_value(
                    canonical_field,
                    data_pool,
                    placeholder=placeholder,
                    mapping_item=item,
                    master_name=master_name,
                )
            except Exception as err:
                # fail-safe: don't crash replacement building
                derived = None

            if derived is not None and derived != "":
                value = str(derived)

        # 3. if still missing and system source type, call system resolver
        if (
            (
                value is None
                or value == ""
            )
            and source_type == "SYSTEM"
        ):
            value = resolve_system_value(
                canonical_field
            )

        if value is None or value == "":
            unresolved.append(
                {
                    "placeholder": placeholder,
                    "canonical_field": (
                        canonical_field
                    ),
                    "reason": (
                        "Chưa có giá trị cho "
                        f"Source Type "
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

    replacements, unresolved = (
        build_replacements(
            packet,
            mapping,
        )
    )

    print(
        f"Đã tạo {len(replacements)} "
        f"nội dung thay thế."
    )
    print("=" * 70)

    for placeholder, value in list(
        replacements.items()
    )[:30]:
        print(
            f"{placeholder} -> {value}"
        )

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
