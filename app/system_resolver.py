from datetime import datetime


def resolve_system_value(canonical_field: str) -> str | None:
    now = datetime.now()

    system_values = {
        "document_year": str(now.year),
        "document_month": f"{now.month:02d}",
        "document_day": f"{now.day:02d}",
        "current_date": now.strftime("%d/%m/%Y"),
        "current_datetime": now.strftime("%d/%m/%Y %H:%M:%S"),
    }

    return system_values.get(canonical_field)