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
		regex = r"(?:"

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


	charm0 = "^" + magic(grammars, rules, 0) + "$"
	scroll0 = re.compile(charm0)
	
	charm31 = magic(grammars, rules, 31)
	charm42 = magic(grammars, rules, 42)
	
	scroll11 = r"^" + charm42 + r"+" + charm31 + r"+$"
	scroll11 = re.compile(scroll11)
	
	scroll31 = re.compile(charm31)
	scroll42 = re.compile(charm42)
	count = 0
	
	for ba in abba:

		baab = [ba[i:i+8] for i in range(0, len(ba), 8)]

		c31 = 0
		c42 = 0
		end42 = False

		for ab in baab:

			if not end42:
				if scroll42.fullmatch(ab) is not None:
					c42 += 1
				else:
					end42 = True
			
			if end42:
				if scroll31.fullmatch(ab) is not None:
					c31 += 1
				else:
					break

		if c42 > c31 and c31 > 0 and c42 + c31 == len(baab):
			count += 1
			continue
	
	print(f"The number of matching patterns is {count}")



if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
