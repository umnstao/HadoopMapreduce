#!/usr/bin/python
import sys
import csv

def mapper():
	reader = csv.reader(sys.stdin, delimiter='\t')
	writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

	for line in reader:
		if len(line) != 19:
			continue
		nodeid, title, tagnames, \
		author_id,body, node_type, parent_id,\
		abs_parent_id, added_at,score,state_string,\
		last_edited_id,last_activity_by_id,last_activity_at,\
		active_revision_id,extra,extra_ref_id,extra_count,marked = line

		if author_id == "author_id":
			continue
		if node_type != "question":
			continue
		tagnames = tagnames.split()
		for tagname in tagnames:
			print "{0}\t{1}".format(tagname, 1)

if __name__ == '__main__':
	mapper()