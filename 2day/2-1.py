#!/usr/bin/python3

import sys

input_file = "input-d2.txt"

if len(sys.argv) > 1:
	input_file = sys.argv[1]


def check_pass(rule, char, pwd):
	count = pwd.count(char)

	return count >= rule[0] and count <= rule[1]


def main():
	valid_pwds = 0

	with open(input_file, "r") as fp:
		
		for line in fp:
			
			parts = line.split()
			rules = list(map(int, parts[0].split('-')))

			if check_pass(rules, parts[1][0], parts[2]):
				valid_pwds += 1

	print(f"The number of valid passwords is: {valid_pwds}")

main()
