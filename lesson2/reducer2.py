#!/usr/bin/python

import sys
def reducer():
    sales_highest = 0
    old_store = None

    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) != 2:
            continue
        store, sales = data
        sales = float(sales)
        if not old_store:
            old_store = store
            sales_highest = sales
            continue
        if old_store == store:
            if sales > sales_highest:
                sales_highest = sales
        else:
            print old_store, "\t", sales_highest
            old_store = store
            sales_highest = sales

if __name__ == '__main__':
    reducer()
