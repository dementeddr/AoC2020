#!/usr/bin/python3

import sys
import xmas


day = 9 #Advent of Code day

def main(input_file):

	encoding = 25
	input_data = []

	with open(input_file, "r") as fp:
		for line in fp:
			input_data.append(int(line))

	code = xmas.XMAS(input_data[:encoding])

	for num in input_data[encoding:]:
		print(f"Code Data: {code.data}\nCode Table:\n{code}")
		if not code.check_number(num):
			print(f"The number that doesn't fit the pattern is {num}")
			break
		else:
			code.increment(num)

if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
