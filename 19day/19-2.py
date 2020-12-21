#!/usr/bin/python3

import sys
import re

day = 19 #Advent of Code day


def magic(grammars, rules, gram):

	if gram in grammars:
		return grammars[gram]

	spread = rules[gram].split()
	regex = r''
	if '|' in spread:
		regex = r"("

	for s in spread:
		if s == '|':
			regex += r'|'
		elif s.isdigit():
			regex += magic(grammars, rules, int(s))
		else:
			print(f"ERROR: I don't know how to deal with '{s}'")

	if '|' in spread:
		regex += r')'

	grammars[gram] = regex

	#print(regex)
	return regex

			

def main(input_file):

	data = ''
	grammarye = re.compile(r"(\d+): (.+)")

	with open(input_file, "r") as fp:
		data = fp.read().split('\n\n')

	abba = data[1].split('\n')
	
	rules = {}
	bases = []
	grammars = {}


	for g in data[0].split('\n'):

		obj = grammarye.match(g)
		num = int(obj.group(1))
		text = obj.group(2)
		rules[num] = text
		
		if '"' in text:
			grammars[num] = text[1]

	for g in sorted(rules.keys()):
		print(f"{g:>3}: {rules[g]}")

	charm = r"^" + magic(grammars, rules, 0) + r"$"
	pattern = re.compile(charm)
	count = 0

	for ba in abba:
		if pattern.match(ba) is not None:
			count += 1
			#print(f"Match! {ba}  {pattern.match(ba).groups()}")
		#else:
			#print(f"NoMa   {ba}")
	
	print(f"The number of matching patterns is {count}")



if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
