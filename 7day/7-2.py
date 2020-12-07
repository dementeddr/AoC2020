#!/usr/bin/python3

import sys
import re
from bag import BagRule

	
def get_containing(color, bag_rules):

	count_add = 1

	for c_color in bag_rules[color].contains:
		count_add += get_containing(c_color, bag_rules) * bag_rules[color].contains[c_color]
	
	return count_add


def main(input_file):
	input_lines = []
	bag_rules = {}

	rule_pat = re.compile(r"(\d* ?[a-z]+ [a-z]+) bag")

	with open(input_file, "r") as fp:
		for line in fp:
			rule_mat = rule_pat.findall(line)
			input_lines.append(rule_mat)
		
			bag = BagRule(rule_mat[0])
			bag_rules[rule_mat[0]] = bag

	for line in input_lines:

		if line[1] == " no other":
			continue

		for rule in line[1:]:
			c_num, c_color = rule.split(' ', 1)

			bag_rules[line[0]].contains[c_color] = int(c_num)
			bag_rules[c_color].inside[line[0]] = int(c_num)

	bag_count = get_containing("shiny gold", bag_rules) - 1 #Because it's counting the shiny gold bag itself

	print(f"The number of bags that a shiny gold bag contains is {bag_count}")


if __name__ == "__main__":
	input_file = "input-d7.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
