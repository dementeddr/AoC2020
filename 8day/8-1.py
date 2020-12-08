#!/usr/bin/python3

import sys

day = 8 #Advent of Code day

def main(input_file):

	insts = []

	with open(input_file, "r") as fp:
		insts = fp.readlines()

	touched = [None for i in range(len(insts))]
	accumulator = 0
	ic = 0

	while touched[ic] is None:
		touched[ic] = ic

		if 	 insts[ic][:3] == "acc":
			accumulator += int(insts[ic][4:])
			ic += 1
		elif insts[ic][:3] == "nop":
			ic += 1
		elif insts[ic][:3] == "jmp":
			ic += int(insts[ic][4:])

	print(f"Boot sequence repeats at IC {ic}. Accumulator = {accumulator}")

if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
