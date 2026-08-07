import json
from pathlib import Path


def save_report(report):
    project_root = Path(__file__).parent.parent
    reports_folder = project_root / "reports"

    reports_folder.mkdir(exist_ok=True)

    output_file = reports_folder / "security_report.json"

    with open(output_file, "w") as file:
        json.dump(report, file, indent=4)

    print(f"\nReport saved to {output_file}")