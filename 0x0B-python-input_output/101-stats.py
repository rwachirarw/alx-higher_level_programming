#!/usr/bin/python3

"""
Write a script that reads stdin line by line and computes metrics:

    Input format: <IP Address> - [<date>] "GET /projects/260 \
        HTTP/1.1" <status code> <file size>
    Each 10 lines and after a keyboard interruption (CTRL + C),\
          prints those statistics since the beginning:
        Total file size: File size: <total size>
        where is the sum of all previous (see input format above)
        Number of lines by status code:
            possible status code: 200, 301, 400, 401, 403, 404, \
                405 and 500
            if a status code doesn’t appear, don’t print anything \
                for this status code
            format: <status code>: <number>
            status codes should be printed in ascending order

"""


def print_stats(size, status_codes):
    """_summary_

    Args:
        size (_type_): _description_
        status_codes (_type_): _description_
    """
    print("File size:", size)
    for key in sorted(status_codes):
        print(key + ":", status_codes[key])


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    count = 0

    try:
        for line in sys.stdin:
            count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    status_codes[line[-2]] = status_codes.get(line[-2], 0) + 1
            except IndexError:
                pass

            if count == 10:
                print_stats(size, status_codes)
                count = 0

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
