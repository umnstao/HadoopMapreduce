#!/usr/bin/python
import sys

def topK(tag_list,tagname, tag_number):
	if tag_list is None or len(tag_list) <= 10:
		tag_list.append([tagname, tag_number])
		tag_list.sort(key = lambda x:x[1])
	else:
		if tag_number > tag_list[9][1]:
			tag_list.pop()
			tag_list.append([tagname, tag_number])
		tag_list.sort(key = lambda x:x[1], reverse=True)
	return tag_list

def reducer():
	prev_tag = None
	tag_list = []
	tag_number = 0
	for line in sys.stdin:
		data = line.strip().split("\t")
		tagname, num = data
		if prev_tag and prev_tag != tagname:
			tag_list = topK(tag_list, tagname,tag_number)
			prev_tag = tagname
			tag_number = 0
		prev_tag = tagname
		tag_number += float(num)
	if prev_tag:
		tag_list = topK(tag_list,tagname,tag_number)
	for tag in tag_list:
		print tag[0],tag[1]

if __name__ == '__main__':
	reducer()