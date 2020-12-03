#!/usr/bin/python3

import sys
from functools import reduce

input_file = "input-d3.txt"

if len(sys.argv) > 1:
	input_file = sys.argv[1]

hill = []

slopes = {
	(1,1):0,
	(3,1):0,
	(5,1):0,
	(7,1):0,
	(1,2):0,
}


with open(input_file, "r") as fp:
	
	for line in fp:
		hill.append(line[:-1])
		print(hill[-1])


for angle in slopes:

	x_pos=0
	y_pos=0

	for line in hill:

		if y_pos == 0:
			
			if line[x_pos] == '#':
				slopes[angle] += 1

			x_pos = (x_pos + angle[0]) % len(line)
		y_pos = (y_pos + 1) % angle[1]


prod = reduce(lambda a, b: a * b, slopes.values(), 1)

print(f"The product of all the trees your face hits on each of these slopes is {prod}")
