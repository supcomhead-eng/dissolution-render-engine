"""Derived field resolver for render engine.

Implements systematic derivation/alias logic per requirements.
"""
from typing import Any
import re


def resolve_derived_value(
    canonical_field: str,
    data_pool: dict[str, Any],
    placeholder: str | None = None,
    mapping_item: dict[str, Any] | None = None,
    master_name: str | None = None,
) -> str | None:
    """Attempt to derive a value for canonical_field from data_pool.

    Returns string value when derivation is certain, otherwise None.
    """
    if not canonical_field:
        return None

    cf = canonical_field.strip()

    # 1. Authority aliases
    if cf == "business_registration_authority":
        # Alias from reg_authority when present
        v = data_pool.get("reg_authority")
        if v:
            return str(v)
        return None

    # direct pass-throughs (use canonical data if present)
    if cf in ("customs_authority", "tax_authority"):
        v = data_pool.get(cf)
        if v:
            return str(v)
        return None

    # 2. Tax code digits rule
    if cf.startswith("tax_code_digit_"):
        raw = data_pool.get("enterprise_tax_code")
        if not raw:
            return None
        digits = re.findall(r"\d", str(raw))
        if len(digits) < 10:
            return None
        try:
            n = int(cf.rsplit("_", 1)[-1])
        except Exception:
            return None
        if n < 1 or n > len(digits):
            return None
        return digits[n - 1]

    # 3. Generic email
    if cf == "generic_email":
        # Priority: company_contact_email, then authorized_person_email (if placeholder is for authorized person)
        company_email = data_pool.get("company_contact_email")
        auth_email = data_pool.get("authorized_person_email")

        if company_email:
            return str(company_email)

        # determine if placeholder refers to authorized person
        refers_to_authorized = _placeholder_refers_to_authorized(placeholder, mapping_item, master_name)
        if refers_to_authorized and auth_email:
            return str(auth_email)

        return None

    # 4. Generic phone number
    if cf in ("generic_phone", "generic_phone_number"):
        company_phone = data_pool.get("company_contact_phone")
        auth_phone = data_pool.get("authorized_person_phone")

        if company_phone:
            return str(company_phone)

        refers_to_authorized = _placeholder_refers_to_authorized(placeholder, mapping_item, master_name)
        if refers_to_authorized and auth_phone:
            return str(auth_phone)

        return None

    # 5. Director name
    if cf == "director_name":
        title = data_pool.get("legal_representative_title") or ""
        name = data_pool.get("legal_representative_name")
        if not name or not title:
            return None
        t = str(title).lower()
        if "giám đốc" in t or "tổng giám đốc" in t:
            return str(name)
        return None

    # 6. Person honorific
    if cf == "person_honorific":
        # If placeholder refers to authorized person, use authorized_person_gender
        if _placeholder_refers_to_authorized(placeholder, mapping_item, master_name):
            g = data_pool.get("authorized_person_gender")
            return _gender_to_honorific(g)

        g = data_pool.get("legal_representative_gender")
        return _gender_to_honorific(g)

    # 7. Signing place
    if cf == "signing_place":
        addr = data_pool.get("registered_office_address")
        if not addr:
            return None
        return _extract_place_from_address(str(addr))

    # default: nothing derived
    return None


def _gender_to_honorific(gender: Any) -> str | None:
    if not gender:
        return None
    s = str(gender).strip().lower()
    if s == "nam":
        return "Ông"
    if s == "nữ" or s == "nu":
        return "Bà"
    return None


def _placeholder_refers_to_authorized(
    placeholder: str | None,
    mapping_item: dict[str, Any] | None,
    master_name: str | None,
) -> bool:
    """Heuristic to decide if placeholder is in the context of an authorized person.

    Conservative: only return True when mapping_item or placeholder text explicitly
    mentions authorized person keywords or master suggests a 'GIAY_GIOI_THIEU' (introduction letter).
    """
    if not placeholder and not mapping_item and not master_name:
        return False

    ph = (placeholder or "").upper()
    if "NGƯỜI UQ" in ph or "NGƯỜI ỦY QUYỀN" in ph or "NGƯỜI ĐƯỢC ỦY QUYỀN" in ph or "NGUOI UQ" in ph:
        return True

    if mapping_item:
        desc = (mapping_item.get("description") or "")
        notes = (mapping_item.get("notes") or "")
        txt = f"{desc}\n{notes}".upper()
        if "NGƯỜI ĐƯỢC ỦY QUYỀN" in txt or "NGƯỜI UỶ QUYỀN" in txt or "NGƯỜI UQ" in txt:
            return True

    if master_name:
        mn = master_name.upper()
        # For customs introduction masters prefer company contact, but still consider explicit authorized masters
        if "GIAY_GIOI_THIEU" in mn or "GIẤY GIỚI THIỆU" in mn:
            # introduction letters often relate to authorized person but we keep conservative policy
            # return False here to prefer company contact unless placeholder explicitly mentions authorized
            return False

    return False


def _extract_place_from_address(address: str) -> str | None:
    """Extract the province/city name from registered_office_address.

    Conservative extraction: look for component immediately before ', Việt Nam' or words 'Thành phố' / 'Tỉnh'.
    """
    parts = [p.strip() for p in address.split(",") if p.strip()]
    if not parts:
        return None

    # If last component contains 'Việt' assume previous part is the location
    last = parts[-1]
    if last.lower().startswith("việt") and len(parts) >= 2:
        candidate = parts[-2]
    else:
        # fallback: try to find tokens like 'Thành phố X' or 'Tỉnh X'
        candidate = address

    # remove leading words
    candidate = re.sub(r"^(Thành phố|TP\.|Tỉnh|TTP\.)\s*", "", candidate, flags=re.IGNORECASE)
    candidate = candidate.strip()

    # if candidate still contains too many commas or slashes, be conservative
    if "," in candidate or "(" in candidate or ";" in candidate:
        # don't attempt risky parsing
        pass

    # minimal sanity: candidate should be short (<= 40 chars) and contain letters
    if 0 < len(candidate) <= 40 and re.search(r"[\p{L}A-Za-z0-9]", candidate):
        return candidate

    # final attempt: search for 'Thành phố X' or 'Tỉnh X' anywhere
    m = re.search(r"(?:Thành phố|Tỉnh)\s+([\w\sÀ-ỹ]+?)(?:,|$)", address, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip()

    return None
