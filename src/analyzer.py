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



def get_severity(count):

    if count >= 10:
        return "HIGH"

    elif count >= 5:
        return "MEDIUM"

    else:
        return "LOW"



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



    suspicious_ips = {}


    for ip, count in failed_by_ip.items():

        suspicious_ips[ip] = {
            "attempts": count,
            "severity": get_severity(count)
        }



    return {
        "failed_attempts": failed_attempts,
        "suspicious_ips": suspicious_ips
    }
    