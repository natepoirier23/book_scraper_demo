import csv
import json

def write_to_csv(data: list[dict], filename: str):
    """
    Write a list of dictionaries to CSV with dynamic fieldnames.
    """
    if not data:
        print("[CSV] No data to write.")
        return

    fieldnames = sorted(data[0].keys())

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"[CSV] Wrote {len(data)} rows to {filename}")


def write_to_json(data: list[dict], filename: str):
    """
    Write list of dictionaries to JSON.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"[JSON] Wrote {len(data)} records to {filename}")
