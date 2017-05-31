#!/usr/bin/python

import sys
def reducer():
    oldfile = None
    total_hits = 0

    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) != 2:
            continue
        thisfile, hits = data
        if oldfile and oldfile != thisfile:
            print oldfile, total_hits
            oldfile = thisfile
            total_hits = 0
        oldfile = thisfile
        total_hits += float(hits)

    if oldfile:
        print oldfile, total_hits

if __name__ == '__main__':
    reducer()
