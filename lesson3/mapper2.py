#!/usr/bin/python
import sys

def mapper():
    for line in sys.stdin:
        data = line.strip().split(" ")
        if len(data) == 10:
            ip, id, name, time, zone, request, filename, web, code, size = data
            print "{0}\t{1}".format(ip,1)
if __name__ == '__main__':
    mapper()
