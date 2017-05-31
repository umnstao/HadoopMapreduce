#!/usr/bin/python
import sys

def reducer():
	prev_nodeid = None
	student_list = []
	for line in sys.stdin:
		data = line.strip().split("\t")
		if len(data) != 2:
			continue
		nodeid, student = data
		if prev_nodeid and prev_nodeid != nodeid:
			print prev_nodeid, student_list
			student_list = []
			prev_nodeid = nodeid
		prev_nodeid = nodeid
		student_list.append(student)

	if prev_nodeid:
		print prev_nodeid, student_list

if __name__ == '__main__':
	reducer()