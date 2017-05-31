#!/usr/bin/python

import sys
def reducer():
    oldip = None
    total_hits = 0

    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) != 2:
            continue
        thisip, hits = data
        if oldip and oldip != thisip:
            print oldip, total_hits
            oldip = thisip
            total_hits = 0
        oldip = thisip
        total_hits += float(hits)

    if oldip:
        print oldip, total_hits

if __name__ == '__main__':
    reducer()
