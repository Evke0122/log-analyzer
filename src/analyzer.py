# -----------------------------
# This file looks for suspicious activity in parsed logs.
# -----------------------------

def analyze_logs(parsed_logs):

    failed_attempts = 0

    failed_by_ip = {}

    for log in parsed_logs:

        if log["status"] == "FAILED":

            failed_attempts += 1


            ip = log["ip"]

            if ip in failed_by_ip:

                failed_by_ip[ip] += 1

            else:

                failed_by_ip[ip] = 1



    return {
        "failed_attempts": failed_attempts,
        "failed_by_ip": failed_by_ip
    }