#!/usr/bin/python

import sys
def reducer():
    sales_total = 0
    old_item = None

    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) != 2:
            continue
        item, sales = data
        if old_item and old_item != item:
            print "{0}\t{1}".format(old_item, sales_total)
            old_item = item
            sales_total = 0
        old_item = item
        sales_total += float(sales)

    if old_item:
        print "{0}\t{1}".format(old_item, sales_total)

if __name__ == '__main__':
    reducer()
