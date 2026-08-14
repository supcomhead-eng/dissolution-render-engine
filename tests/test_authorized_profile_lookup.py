import pytest
from app.authorized_profile_loader import find_authorized_profile
from app.replacement_builder import build_data_pool


def test_profile_contains_issue_date_and_no_issue_place():
    # find profile by alias (case-insensitive, accent-insensitive)
    profile = find_authorized_profile("quốc Hưng")

    # profile should contain authorized_person_id_issue_date per profiles JSON
    assert "authorized_person_id_issue_date" in profile
    assert profile["authorized_person_id_issue_date"] == "09/09/2022"

    # profile does not include authorized_person_id_issue_place in current data
    assert "authorized_person_id_issue_place" not in profile


def test_build_data_pool_includes_profile_date():
    packet = {
        "canonical_data": {},
        "authorized_person": {"name": "Quốc Hưng"},
    }

    data_pool = build_data_pool(packet)

    # authorized_person_id_issue_date should be present in data_pool (formatted)
    assert data_pool.get("authorized_person_id_issue_date") == "09/09/2022"

    # and issue place should not be auto-filled
    assert data_pool.get("authorized_person_id_issue_place") is None
