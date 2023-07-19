#!/usr/bin/python3
"""
<<<<<<< HEAD
This module contains the function that displays the
stats from the standard input
"""
import re
import sys
status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                403: 0, 404: 0, 405: 0, 500: 0}
print_counter = 0
size_summation = 0


def print_logs():
    """
    Prints status codes to the logs
    """
    print("File size: {}".format(size_summation))
    for k, v in sorted(status_codes.items()):
        if v != 0:
            print("{}: {}".format(k, v))


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            std_line = line.replace("\n", "")
            log_list = re.split('- | "|" | " " ', str(std_line))
            try:
                codes = log_list[-1].split(" ")
                if int(codes[0]) not in status_codes.keys():
                    continue
                status_codes[int(codes[0])] += 1
                print_counter += 1
                size_summation += int(codes[1])
                if print_counter % 10 == 0:
                    print_logs()
            except():
                pass
        print_logs()
    except KeyboardInterrupt:
        print_logs()
=======
Log parsing
"""

import sys

if __name__ == '__main__':

    filesize, count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}

    def print_stats(stats: dict, file_size: int) -> None:
        print("File size: {:d}".format(filesize))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass
            try:
                filesize += int(data[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                print_stats(stats, filesize)
        print_stats(stats, filesize)
    except KeyboardInterrupt:
        print_stats(stats, filesize)
        raise
>>>>>>> e8795977d0c2981e8df559756d5c54a1966a7ed3
