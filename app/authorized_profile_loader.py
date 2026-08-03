import json
import unicodedata
from pathlib import Path
from typing import Any


PROFILE_FILE = Path(
    "profiles/authorized_profiles.json"
)


DATE_FIELDS = (
    "authorized_person_date_of_birth",
    "authorized_person_id_issue_date",
    "authorized_person_id_expiry_date",
)


def normalize_name(value: str) -> str:
    """
    Chuẩn hóa tên để so sánh:
    - không phân biệt hoa/thường;
    - không phân biệt có dấu/không dấu;
    - bỏ khoảng trắng thừa.
    """
    value = value.strip().casefold()

    normalized = unicodedata.normalize(
        "NFD",
        value,
    )

    without_accents = "".join(
        character
        for character in normalized
        if unicodedata.category(character) != "Mn"
    )

    return " ".join(
        without_accents.split()
    )


def format_date_ddmmyyyy(
    value: Any,
) -> str:
    text = str(value or "").strip()

    if (
        len(text) == 10
        and text[4] == "-"
        and text[7] == "-"
    ):
        year, month, day = text.split("-")

        if (
            year.isdigit()
            and month.isdigit()
            and day.isdigit()
        ):
            return f"{day}/{month}/{year}"

    return text


def format_profile_dates(
    profile: dict[str, Any],
) -> dict[str, Any]:
    formatted_profile = dict(profile)

    for field in DATE_FIELDS:
        if field in formatted_profile:
            formatted_profile[field] = (
                format_date_ddmmyyyy(
                    formatted_profile.get(field)
                )
            )

    return formatted_profile


def load_authorized_profiles() -> list[dict[str, Any]]:
    if not PROFILE_FILE.exists():
        raise FileNotFoundError(
            f"Không tìm thấy file profile: "
            f"{PROFILE_FILE}"
        )

    with PROFILE_FILE.open(
        "r",
        encoding="utf-8",
    ) as file:
        data = json.load(file)

    profiles = data.get("profiles", [])

    if not isinstance(profiles, list):
        raise ValueError(
            "Trường profiles trong JSON "
            "phải là một danh sách."
        )

    valid_profiles: list[dict[str, Any]] = []

    for profile in profiles:
        if isinstance(profile, dict):
            valid_profiles.append(profile)

    return valid_profiles


def find_authorized_profile(
    person_name: str,
) -> dict[str, Any]:
    if not person_name.strip():
        raise ValueError(
            "Tên người được ủy quyền đang trống."
        )

    query = normalize_name(person_name)
    profiles = load_authorized_profiles()

    for profile in profiles:
        aliases = profile.get("aliases", [])

        if not isinstance(aliases, list):
            aliases = []

        candidates = [
            profile.get(
                "authorized_person_name",
                "",
            ),
            *aliases,
        ]

        normalized_candidates = {
            normalize_name(str(candidate))
            for candidate in candidates
            if str(candidate).strip()
        }

        if query in normalized_candidates:
            return format_profile_dates(
                profile
            )

    available_names = [
        str(
            profile.get(
                "authorized_person_name",
                "",
            )
        )
        for profile in profiles
        if str(
            profile.get(
                "authorized_person_name",
                "",
            )
        ).strip()
    ]

    raise ValueError(
        f"Không tìm thấy profile cho: "
        f"{person_name}. "
        f"Profile hiện có: "
        f"{', '.join(available_names)}"
    )


def main() -> None:
    test_name = "quốc hưng"

    profile = find_authorized_profile(
        test_name
    )

    print("TÌM PROFILE THÀNH CÔNG")
    print("=" * 70)

    for key, value in profile.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()