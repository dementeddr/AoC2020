#!/usr/bin/python3

import sys

input_file = "input-d3.txt"

if len(sys.argv) > 1:
	input_file = sys.argv[1]

trees = 0
angle = 3
x = 0

with open(input_file, "r") as fp:
	
	for line in fp:
		
		if line[x] == '#':
			trees += 1

		x = (x + angle) % (len(line)-1)

print(f"At angle {angle}, your face will hit {trees} trees on the way down")


