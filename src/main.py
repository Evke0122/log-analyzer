from log_parser import parse_log_line


def load_logs():

    file_path = "../logs/auth.log"

    with open(file_path, "r") as file:

        lines = file.readlines()

    return lines



def main():

    print("Security Log Analyzer")
    print("---------------------")


    logs = load_logs()


    print("\nParsed logs:\n")


    for line in logs:

        result = parse_log_line(
            line.strip()
        )


        print(result)



if __name__ == "__main__":
    main()