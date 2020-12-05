#!/usr/bin/python

import sys
import re

input_file = "input-d4.txt"

doc_fields = re.compile(r"(\w{3}):(\S+)")
v_year = re.compile(r"^(\d{4})$")

regexes = {
	'byr': v_year,
	'iyr': v_year,
	'eyr': v_year,
	'hgt': re.compile(r"^(\d{2,3})(in|cm)$"),
	'hcl': re.compile(r"^#([0-9a-f]{6})$"),
	'ecl': re.compile(r"^(amb|blu|brn|gry|grn|hzl|oth)$"),
	'pid': re.compile(r"^(\d{9})$"),
}

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



def validate(doc):

	isValid = True

	for field in doc:
		
		data = doc[field]

		if	 field == "cid":
			continue
		elif data is None:
			isValid = False
			break

		val = regexes[field].match(data)

		if	 val is None:
			isValid = False
			break

		elif field == "byr":
			if int(val.group(0)) < 1920 or int(val.group(0)) > 2002:
				isValid = False
				break

		elif field == "iyr":
			if int(val.group(0)) < 2010 or int(val.group(0)) > 2020:
				isValid = False
				break

		elif field == "eyr":
			if int(val.group(0)) < 2020 or int(val.group(0)) > 2030:
				isValid = False
				break

		elif field == "hgt":
			if 	 val.group(1) == 'in':
				if int(val.group(0)) < 59 or int(val.group(0)) > 76:
					isValid = False
					break
			elif val.group(1) == 'cm':
				if int(val.group(0))[0] < 150 or int(val.group(0))[0] > 193:
					isValid = False
					break

		elif field == "hcl":
			continue #regex does full validation

		elif field == "ecl":
			continue #regex does full validation

		elif field == "pid":
			continue #regex does full validation
			
		else:
			print("ERROR: Invalid field {field}")

	return isValid



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

	if validate(doc):
		num_valid += 1
		print(f"Valid!  {doc['hgt']}")

print(f'There are {num_valid} valid "passports" in the queue')
