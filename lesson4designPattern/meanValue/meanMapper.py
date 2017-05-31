#!/usr/bin/python

import sys
from datetime import datetime

def mapper():
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) == 6:
            data, time, store, item, cost, payment = data
            day = datetime.striptime(date, "%Y-%m-%d").weekday()
            print "{0}\t{1}".format(day,cost)

if __name__ == '__main__':
    mapper()
