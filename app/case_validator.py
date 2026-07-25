from typing import Any


def validate_case(case: dict[str, Any]) -> list[str]:
    warnings: list[str] = []

    required_master_codes = {
        item["master_code"]
        for item in case.get("required_masters", [])
    }

    generation_order = case.get("generation_order", [])

    for master_code in generation_order:
        if master_code not in required_master_codes:
            warnings.append(
                f"{master_code} có trong Generation Order "
                f"nhưng không có trong Required Masters."
            )

    for master_code in required_master_codes:
        if master_code not in generation_order:
            warnings.append(
                f"{master_code} có trong Required Masters "
                f"nhưng không có trong Generation Order."
            )

    if not case.get("case_id"):
        warnings.append("Thiếu case_id.")

    if not case.get("case_name"):
        warnings.append("Thiếu case_name.")

    if not case.get("company_types"):
        warnings.append("Thiếu company_types.")

    return warnings