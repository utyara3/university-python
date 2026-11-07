import math
import os
import re
import sys
from collections import defaultdict
from datetime import datetime

clf_pattern = re.compile(
    r"(?P<ip>\S+)\s+"
    r"(?P<client_id>\S+)\s+"
    r"(?P<user>\S+)\s+"
    r"\[(?P<timestamp>[^\]]+)\]\s+"
    r'"(?P<method>\S+)\s+'
    r'(?P<request>[^\s"]+)\s*'
    r'(?P<protocol>[^"]*)"\s+'
    r"(?P<status>\d{3})\s+"
    r"(?P<size>\S+)"
)

LOG_TIME_FORMAT = "%d/%b/%Y:%H:%M:%S %z"


def get_log_file_path() -> str:
    log_file_path = input("Enter path to log file: ")

    if not os.path.exists(log_file_path) or not os.path.isfile(log_file_path):
        sys.exit(f"Error: '{log_file_path}' must be an existing file!")

    return log_file_path


def get_time_range() -> tuple[datetime, datetime]:
    print("\nEnter time range (Format example: 12/Oct/2025:10:20:48 +0300)")
    while True:
        try:
            start_str = input("Enter START timestamp: ").strip()
            start_time = datetime.strptime(start_str, LOG_TIME_FORMAT)  # noqa
            break
        except ValueError:
            print("Invalid format! Please match the log timestamp format precisely.")

    while True:
        try:
            end_str = input("Enter END timestamp: ").strip()
            end_time = datetime.strptime(end_str, LOG_TIME_FORMAT)  # noqa
            break
        except ValueError:
            print("Invalid format! Please match the log timestamp format precisely.")

    return start_time, end_time


def file_analysis(file_path: str, start_time: datetime, end_time: datetime):
    size_by_status = defaultdict(list)
    num_of_errors = 0

    range_total_requests = 0
    range_num_of_errors = 0
    range_size_by_status = defaultdict(list)

    with open(file_path, "r", encoding="utf-8", errors="ignore") as log_file:
        for line_num, line in enumerate(log_file, 1):
            line = line.strip()
            if not line:
                continue

            match = clf_pattern.match(line)
            if match:
                log_data = match.groupdict()

                status_code = int(log_data["status"])

                raw_size = log_data["size"]
                size = 0 if raw_size == "-" else int(raw_size)

                size_by_status[status_code].append(size)
                if 400 <= status_code < 600:
                    num_of_errors += 1

                try:
                    log_timestamp = datetime.strptime(  # noqa
                        log_data["timestamp"], LOG_TIME_FORMAT
                    )
                    if start_time <= log_timestamp <= end_time:
                        range_total_requests += 1
                        range_size_by_status[status_code].append(size)
                        if 400 <= status_code < 600:
                            range_num_of_errors += 1
                except ValueError:
                    print(f"Line {line_num} has an invalid timestamp format")
            else:
                print(f"Line {line_num} does not match the CLF format")

    average_bytes = {k: math.ceil(sum(v) / len(v)) for k, v in size_by_status.items()}

    range_average_bytes = {
        k: math.ceil(sum(v) / len(v)) for k, v in range_size_by_status.items()
    }

    time_range_stats = {
        "total_requests": range_total_requests,
        "errors": range_num_of_errors,
        "average_bytes_by_status": range_average_bytes,
    }

    return average_bytes, num_of_errors, time_range_stats


def write_results_to_file(
    output_path: str, average_bytes: dict, num_of_errors: int, time_range_stats: dict
):
    try:
        with open(output_path, "w", encoding="utf-8") as out_file:
            out_file.write("a. Average response size by status code:\n")

            out_file.writelines(
                (
                    f"  Status {status}: {avg_size} bytes\n"
                    for status, avg_size in sorted(average_bytes.items())
                )
            )
            out_file.write(
                f"\nb. Total number of client/server errors (4XX, 5XX): {num_of_errors}\n"
            )

            out_file.write(
                "\nc. Statistics collected within the specified time range:\n"
            )
            out_file.write(
                f"  Total requests in range: {time_range_stats['total_requests']}\n"
            )
            out_file.write(
                f"  Errors (4XX, 5XX) in range: {time_range_stats['errors']}\n"
            )
            out_file.write("  Average response size by status code in range:\n")
            if time_range_stats["average_bytes_by_status"]:
                out_file.writelines(
                    (
                        f"    Status {status}: {avg_size} bytes\n"
                        for status, avg_size in sorted(
                            time_range_stats["average_bytes_by_status"].items()
                        )
                    )
                )
            else:
                out_file.write("    No requests found within this time range\n")

        print(f"\nSuccess: Analysis report successfully written to '{output_path}'")
    except OSError as e:
        print(f"Error: Could not write to output file. {e}")


if __name__ == "__main__":
    log_file_path = get_log_file_path()
    start_time, end_time = get_time_range()

    print("analysing file")
    average_bytes, num_of_errors, time_range_stats = file_analysis(
        log_file_path, start_time, end_time
    )

    output_file_path = "analysis_report.txt"
    write_results_to_file(
        output_file_path, average_bytes, num_of_errors, time_range_stats
    )
