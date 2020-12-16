#!/usr/bin/python3

import sys
import re

day = 16 #Advent of Code day


def isValid(num, fields):
	
	for rule in fields:
		if num >= rule[0] and num <= rule[1]:
			return True

	return False



def main(input_file):

	field_lims = re.compile(f"(\d+)")

	with open(input_file, "r") as fp:
		data = fp.read().split('\n\n')

	fields = []
	
	for line in data[0].split('\n'):
		match = field_lims.findall(line)
		fields.append((int(match[0]), int(match[1])))
		fields.append((int(match[2]), int(match[3])))

	tickets = data[2].split('\n')[1:-1]
	error = 0

	for line in tickets:
		nums = list(map(int, line.split(',')))
		
		for n in nums:
			if not isValid(n, fields):
				error += n

	print(f"Your error rate is {error}")



if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
