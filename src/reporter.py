# -----------------------------
# Report Generator
# Saves security analysis results into a JSON file.
# -----------------------------

import json


def save_report(report):

    output_file = "../reports/security_report.json"

    with open(output_file, "w") as file:

        json.dump(
            report,
            file,
            indent=4
        )


    print(
        f"\nReport saved to {output_file}"
    )