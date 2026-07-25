import json
from pathlib import Path
from typing import Any


DECISION_PACKET_FILE = Path("input/decision_packet_test.json")


def load_decision_packet(file_path: Path) -> dict[str, Any]:
    if not file_path.exists():
        raise FileNotFoundError(
            f"Không tìm thấy Decision Packet: {file_path}"
        )

    with file_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, dict):
        raise ValueError("Decision Packet phải là một JSON object.")

    return data


def main() -> None:
    packet = load_decision_packet(DECISION_PACKET_FILE)

    canonical_data = packet.get("canonical_data", {})
    selected_masters = packet.get("selected_masters", [])

    print("ĐỌC DECISION PACKET THÀNH CÔNG")
    print("=" * 60)

    print("\nCANONICAL DATA:")
    for field_name, value in canonical_data.items():
        print(f"{field_name}: {value}")

    print("\nSELECTED MASTERS:")
    for master in selected_masters:
        print(master.get("master_name"))


if __name__ == "__main__":
    main()