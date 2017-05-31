#!/usr/bin/python
import sys

def reducer():
	prev_user = None
	for line in sys.stdin:
		data = line.strip().split("\t")
		if len(data) == 9:
			user, dummy, title, \
			tagnames, node_type, parent_id, abs_parent_id, \
			added_at, score = data

		if len(data) == 6:
			user, dummy, reputation, gold, silver, bronze = data

		if prev_user and user != prev_user:
				print user, "\t", title,"\t", tagnames, "\t", \
				node_type, "\t", parent_id, "\t", abs_parent_id, \
				"\t", added_at, "\t", score, "\t", reputation, "\t", \
				gold, "\t", silver,"\t", bronze
				prev_user = user
		prev_user = user

	if prev_user:
		print user, "\t", title,"\t", tagnames, "\t", \
		node_type, "\t", parent_id, "\t", abs_parent_id, \
		"\t", added_at, "\t", score, "\t", reputation, "\t", \
		gold, "\t", silver,"\t", bronze

if __name__ == '__main__':
	reducer()