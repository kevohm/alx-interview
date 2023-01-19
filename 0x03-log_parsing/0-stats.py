#!/usr/bin/python3
"""log_parsing"""
import sys
import shlex

def read_stdin():
    """
    reads stdin line by line and computes metrics
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
    """
    count = 0
    file_size = 0
    status = { "200":0,
                "301":0,
                "400":0,
                "401":0,
                "403":0,
                "404":0,
                "405":0,
                "500":0 }
    for line in sys.stdin:
        original = line.rstrip()
        data = shlex.split(original)
        if 7 == len(data):
            count += 1
            file_size += int(data[6])
            if data[5]:
                try:
                    int(data[5])
                    status[data[5]] += 1
                except(e):
                    pass

            if count == 10:
                print("File size: {}".format(file_size))
                for k, v in status.items():
                    if v != 0:
                        print("{}: {}".format(k, v))
                count = 0
                status = { "200":0,
                "301":0,
                "400":0,
                "401":0,
                "403":0,
                "404":0,
                "405":0,
                "500":0 }


read_stdin()
