#!/usr/bin/python3

import sys
from collections import defaultdict

day = 14 #Advent of Code day
word = 36


def write_val(new_val, mem_val, mask):

	assert len(new_val) == word
	assert len(mem_val) == word
	assert len(mask) == word

	for i in range(word):
		if mask[i] == 'X':
			mem_val[i] = new_val[i]
		else:
			mem_val[i] = mask[i]

def pad_val(val):
	while len(val) < word:
		val.insert(0, '0')



def main(input_file):

	mem = defaultdict(lambda : ['0' for i in range(word)])
	mask = ['X' for i in range(word)]

	with open(input_file, "r") as fp:
		
		for line in fp:
			func, _, arg = line.split()
			if func == 'mask':
				mask = list(arg)

			elif func[:3] == 'mem':
				addr = int(func[4:-1])
				val = list(format(int(arg), 'b'))
				pad_val(val)
				write_val(val, mem[addr], mask)
			else:
				print(f"ERROR: Rampant corruption! {line}")

	sum_mem = 0

	for addr in mem:
		sum_mem += int(''.join(mem[addr]), 2)

	print(f"Sum of in-memory values is {sum_mem}")



if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
