#!/usr/bin/python3

import sys
import re
from bag import BagRule


def get_containers(color, bag_types, bag_rules):

	for i_color in bag_rules[color].inside:
		bag_types.add(i_color)
		get_containers(i_color, bag_types, bag_rules)
	return
	

def main(input_file):
	input_lines = []
	bag_rules = {}
	bag_types = set([])

	rule_pat = re.compile(r"(\d* ?[a-z]+ [a-z]+) bag")

	with open(input_file, "r") as fp:
		for line in fp:
			rule_mat = rule_pat.findall(line)
			input_lines.append(rule_mat)
		
			bag = BagRule(rule_mat[0])
			bag_rules[rule_mat[0]] = bag

	for line in input_lines:
		#print(line)

		if line[1] == " no other":
			continue

		for rule in line[1:]:
			c_num, c_color = rule.split(' ', 1)

			bag_rules[line[0]].contains[c_color] = c_num
			bag_rules[c_color].inside[line[0]] = c_num

	#print(bag_rules)

	get_containers("shiny gold", bag_types, bag_rules)

	print(f"The number of bag types that can contain a shiny gold bag is {len(bag_types)}")


if __name__ == "__main__":
	input_file = "input-d7.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
