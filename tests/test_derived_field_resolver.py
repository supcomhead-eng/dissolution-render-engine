import pytest
from app.derived_field_resolver import resolve_derived_value


def make_packet():
    return {
        "decision_packet_version": "0.1",
        "case_summary": {
            "case_request": "giải thể",
            "company_type": "Công ty cổ phần",
            "selected_case_name": "Giải thể công ty cổ phần",
            "status": "needs_confirmation",
        },
        "canonical_data": {
            "company_name": "CÔNG TY CỔ PHẦN XÂY DỰNG DV&TM MINH NGỌC",
            "company_abbreviation": "DV&TM MINH NGỌC",
            "enterprise_tax_code": "0111562780",
            "registered_office_address": "Số 130A, Đường Ngô Quyền, Phường Hà Đông, Thành phố Hà Nội, Việt Nam",
            "company_contact_phone": "0936102879",
            "company_contact_email": "tranquangxaydung77@gmail.com",
            "legal_representative_name": "TRẦN MINH QUANG",
            "legal_representative_gender": "Nam",
            "legal_representative_title": "Giám đốc",
            "reg_authority": "Phòng Đăng ký kinh doanh và Tài chính doanh nghiệp",
            "tax_authority": "cơ quan thuế số 6",
            "customs_authority": "Chi cục Hải quan Khu vực I",
        },
        "authorized_person": {
            "name": "Quốc Hưng",
            "profile_lookup_required": True,
        },
        "selected_masters": [
            {"master_name": "MASTER_GIAY_GIOI_THIEU_HAI_QUAN_CLEAN.docx"}
        ],
    }


def test_authority_alias_and_direct_fields():
    packet = make_packet()
    data_pool = packet["canonical_data"]

    assert resolve_derived_value("business_registration_authority", data_pool) == "Phòng Đăng ký kinh doanh và Tài chính doanh nghiệp"
    assert resolve_derived_value("customs_authority", data_pool) == "Chi cục Hải quan Khu vực I"
    assert resolve_derived_value("tax_authority", data_pool) == "cơ quan thuế số 6"


def test_tax_code_digits():
    packet = make_packet()
    data_pool = packet["canonical_data"]

    expected = list("0111562780")
    for i, ch in enumerate(expected, start=1):
        cf = f"tax_code_digit_{i}"
        assert resolve_derived_value(cf, data_pool) == ch


def test_generic_email_and_phone_and_director_and_honorific_and_signing_place():
    packet = make_packet()
    data_pool = packet["canonical_data"]

    # generic email/phone should pick company contact
    assert resolve_derived_value("generic_email", data_pool, placeholder="[EMAIL]", master_name="MASTER_GIAY_GIOI_THIEU_HAI_QUAN_CLEAN.docx") == "tranquangxaydung77@gmail.com"
    assert resolve_derived_value("generic_phone_number", data_pool, placeholder="[SĐT]", master_name="MASTER_GIAY_GIOI_THIEU_HAI_QUAN_CLEAN.docx") == "0936102879"

    # director name only when title indicates Giám đốc
    assert resolve_derived_value("director_name", data_pool) == "TRẦN MINH QUANG"

    # honorific from gender
    assert resolve_derived_value("person_honorific", data_pool) == "Ông"

    # signing_place extracted from address
    assert resolve_derived_value("signing_place", data_pool) == "Hà Nội"
