#!/usr/bin/python3

import sys

day = 10 #Advent of Code day

def main(input_file):

	adapters = []

	with open(input_file, "r") as fp:
		
		text = fp.readlines()
	
	adapters = sorted(list(map(int, text)))

	count3 = 1
	count2 = 1
	count1 = 1

	for i in range(len(adapters)-1):
		
		diff = adapters[i+1] - adapters[i]

		if	 diff == 1:
			count1 += 1
		elif diff == 3:
			count3 += 1
		else:
			count2 += 2


	print(f"Something something jolts: {count1} x {count3} = {count1 * count3}")
	

if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
