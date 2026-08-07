from log_parser import parse_log_line
from analyzer import analyze_logs
from reporter import save_report



def load_logs():

    file_path = "../logs/auth.log"


    with open(file_path, "r") as file:

        return file.readlines()



def main():

    print("Security Log Analyzer")
    print("---------------------")


    raw_logs = load_logs()


    parsed_logs = []


    # Convert every line into structured data
    for line in raw_logs:

        result = parse_log_line(
            line.strip()
        )


        if result:

            parsed_logs.append(result)



    report = analyze_logs(
        parsed_logs
    )


    print("\nSecurity Report")
    print("----------------")


    print(
        "Failed attempts:",
        report["failed_attempts"]
    )


    print(
        "\nFailed attempts by IP:"
    )


    for ip, count in report["failed_by_ip"].items():

        print(
            ip,
            "->",
            count
        )
        
    save_report(report)

    

if __name__ == "__main__":
    main()