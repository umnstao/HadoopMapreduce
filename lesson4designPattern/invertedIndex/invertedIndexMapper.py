#!/usr/bin/python

import sys
import csv
import re

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        if len(line) != 19:
            continue
        node_id = line[0]
        if node_id == "id":
            continue
        raw_body = line[4]
        body = re.split('\W+', raw_body)
        for word in body:
            word = word.strip()
            word = word.lower()
            print "{0}\t{1}".format(word, node_id)

if __name__ == '__main__':
    mapper()
