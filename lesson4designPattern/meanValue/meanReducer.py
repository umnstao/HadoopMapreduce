#!/usr/bin/python
import sys

def reducer():
    total_cost = 0
    count = 0
    prev_day = None
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) != 2:
            continue
        day, cost = data
        if prev_day and prev_day != day:
            print "{0}\t{1}".format(prev_day, total_cost/count)
            prev_day = day
            total_cost = 0
            count = 0
        prev_day = day
        total_cost += float(cost)
        count += 1
    if prev_day:
        print "{0}\t{1}".format(prev_day, total_cost/count)

if __name__ == '__main__':
    reducer()