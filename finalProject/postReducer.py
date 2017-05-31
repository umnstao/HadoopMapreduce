#!/usr/bin/python
import sys

def reducer():
	prev_node = None
	answerlen = 0
	questionlen = 0
	answernum = 0
	for line in sys.stdin:
		data = line.split("\t")
		if len(data) != 3:
			continue
		cur_node = data[0]
		node_type = data[1]
		bodylen = float(data[2])

		if prev_node and prev_node != cur_node:
			if answernum == 0:
				print prev_node, questionlen, 0
			else:
				print prev_node, questionlen, answerlen/answernum
			prev_node = cur_node
			questionlen = 0
			answerlen = 0
			answernum = 0


		prev_node = cur_node
		if node_type == "question":
			questionlen = bodylen
		else:
			answerlen += bodylen
			answernum += 1

	if prev_node:
		if answernum == 0:
			print prev_node, questionlen, 0
		else:
			print prev_node, questionlen, answerlen/answernum

if __name__ == '__main__':
	reducer()