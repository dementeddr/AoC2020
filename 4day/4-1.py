#!/usr/bin/python3

import sys
import re

input_file = "input-d4.txt"

doc_fields = re.compile(r"(\w{3}):(\S+)")
doc_list = []

if len(sys.argv) > 1:
	input_file = sys.argv[1]

def create_empty_doc():
	return {
		"byr":None,
		"iyr":None,
		"eyr":None,
		"hgt":None,
		"hcl":None,
		"ecl":None,
		"pid":None,
		"cid":None,
	}

def read_one_doc(fp):
	doc_str = ""
	line = "blank"

	while line not in ('\n','',None):
		line = fp.readline()
		doc_str += line.replace('\n', ' ')
	
	if doc_str in ('\n',"",None):
		return None

	doc_form = create_empty_doc()

	for field in doc_fields.findall(doc_str):
		doc_form[field[0]] = field[1]

	return doc_form

		

with open(input_file, "r") as fp:

	doc = None

	while True:
		doc = read_one_doc(fp)
		if doc is None:
			break
		doc_list.append(doc)


num_valid = 0

for doc in doc_list:
	print(doc)

	valid = True

	for field in create_empty_doc():
		if field == "cid":
			continue
		elif doc[field] is None:
			valid = False
			break
	
	if valid:
		num_valid += 1
		#print("Valid!")

print(f'There are {num_valid} valid "passports" in the queue')
