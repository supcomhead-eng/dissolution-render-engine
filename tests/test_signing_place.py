import pytest
from app.derived_field_resolver import resolve_derived_value


def test_signing_place_hanoi():
    data_pool = {
        "registered_office_address": "Số 130A, Đường Ngô Quyền, Phường Hà Đông, Thành phố Hà Nội, Việt Nam"
    }
    assert resolve_derived_value("signing_place", data_pool) == "Hà Nội"


def test_signing_place_bacninh():
    data_pool = {
        "registered_office_address": "Thôn 3, Xã Phú Hòa, Tỉnh Bắc Ninh, Việt Nam"
    }
    assert resolve_derived_value("signing_place", data_pool) == "Bắc Ninh"
