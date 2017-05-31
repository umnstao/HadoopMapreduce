#!/usr/bin/python
import sys

def reducer():
	prev_word = None
	nodelist = []
	for line in sys.stdin:
		data = line.split("\t").strip()
		if len(data) != 2:
			continue
		word = data[0]
		node_id = data[1]
		if prev_word and prev_word != word:
			print prev_word, sorted(nodelist)
			prev_word = word
			nodelist = []
		prev_word = word
		if node_id not in nodelist:
			nodelist.append(node_id)

	if prev_word:
		print prev_word, sorted(nodelist)

if __name__ == '__main__':
	reducer()