#!/usr/bin/python3

import sys
import re

day = 21 #Advent of Code day

def main(input_file):

	data = ''
	#ing_pat = re.compile(r"(\w+ )+")
	#ing_pat = re.compile(r"(\w+ )+\(contains (\w+ )+\)")

	with open(input_file, "r") as fp:
		data = fp.read().split('\n')[:-1]
		
	found = set()
	contains = {}
	all_ingredients = []

	for line in data:
		
		ingr2 = line.split("(contains")
		ingredients = set(ingr2[0].split())
		allergens = ingr2[1].split()
		all_ingredients += ingredients
		
		for a in allergens:
			a = a[:-1]

			if a not in contains:
				contains[a] = ingredients
				continue
			else:
				contains[a] = contains[a] & ingredients

	solving = True

	while solving:
		solving = False

		for c in contains:
			if len(contains[c]) == 1:
				found = found | contains[c]

			else:
				contains[c] -= found
				solving = True
				
	for c in contains:
		print(f"{c:>8}: {next(iter(contains[c]))}")

	count = 0

	for a in all_ingredients:
		if a not in found:
			count += 1

	print(f"The hypoallergenic ingredient count is {count}")
			


if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
