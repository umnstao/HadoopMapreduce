#!/usr/bin/python
import sys

def findmax(all_hours):
	largest = -1
	ret = []
	for i in range(len(all_hours)):
		if all_hours[i] == largest:
			ret.append(i)
		elif all_hours[i] > largest:
			largest = all_hours[i]
			ret = [i]
	return ret

def reducer():
	prev_student_id = None
	all_hours = [0]*24
	for line in sys.stdin:
		data = line.strip().split("\t")
		if len(data) != 2:
			continue
		student_id, hour = data
		hour = int(hour)
		if prev_student_id and prev_student_id != student_id:
			active_hours = findmax(all_hours)
			for active_hour in active_hours:
				print "{0}\t{1}".format(prev_student_id, active_hour)
			prev_student_id = student_id
			all_hours = [0]*24
		prev_student_id = student_id
		all_hours[hour] += 1

	if prev_student_id:
		active_hours = findmax(all_hours)
		for active_hour in active_hours:
			print "{0}\t{1}".format(prev_student_id, active_hour)

if __name__ == '__main__':
	reducer()