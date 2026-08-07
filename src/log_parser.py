
import re


def parse_log_line(line):

    pattern = (
        r"(?P<date>\S+\s+\S+) "
        r"(?P<status>SUCCESS|FAILED) "
        r"user=(?P<username>\w+) "
        r"ip=(?P<ip>\d+\.\d+\.\d+\.\d+)"
    )

    match = re.match(
        pattern,
        line
    )

    if match:

        return match.groupdict()


    return None

