#!/usr/bin/python3

import sys
from collections import defaultdict

day = 14 #Advent of Code day
word = 36


def mask_addr(base_addr, floater, mask):
	masked = base_addr.copy()

	for i in range(word):
		if 	 mask[i] == 'X':
			masked[i] = floater.pop(0)
		elif mask[i] == '1':
			masked[i] = '1'
		elif mask[i] == '0':
			continue
		else:
			print(f"ERROR: No one cared who I was until I screwed up the mask: {mask}")

	return masked



def decode_addrs(base_addr, mask):
	
	assert len(base_addr) == word
	assert len(mask) == word

	variance = mask.count('X')
	addr_spread = []

	for i in range(2**variance):
		floater = list(format(i, 'b'))
		
		while len(floater) < variance:
			floater.insert(0, '0')
		
		addr_spread.append(mask_addr(base_addr, floater, mask))
		
	return addr_spread



def write_to_mem(new_val, mem_addrs, mem):
	for addr in mem_addrs:
		mem[int(''.join(addr),2)] = new_val



def expand_val(val):
	
	ret = list(format(int(val), 'b'))
	while len(ret) < word:
		ret.insert(0, '0')

	return ret



def main(input_file):

	mem = defaultdict(lambda : ['0' for i in range(word)])
	mask = ['X' for i in range(word)]

	with open(input_file, "r") as fp:
		
		for line in fp:
			func, _, arg = line.split()
			if func == 'mask':
				mask = list(arg)

			elif func[:3] == 'mem':
				base_addr = expand_val(func[4:-1])
				val = int(arg)
				mem_addrs = decode_addrs(base_addr, mask)
				write_to_mem(val, mem_addrs, mem)

			else:
				print(f"ERROR: Rampant corruption! {line}")

	sum_mem = 0

	for addr in mem:
		sum_mem += mem[addr]

	print(f"Sum of in-memory values is {sum_mem}")



if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
