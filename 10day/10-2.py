#!/usr/bin/python3

import sys

day = 10 #Advent of Code day



def divvy(adapters):

	groups = []
	chain = []
	prev = 0


	for i in range(1, len(adapters)):
		
		diff = adapters[i] - adapters[i-1]

		if diff == 3:
			chain = adapters[prev:i]
			groups.append(chain)
			prev = i

	groups.append(adapters[prev:])

	return groups



#Do some heavy duty algorithmic calculations involving combinatorics math theory
def combinatorics(group):
	
	if	 len(group) == 1:
		return 1
	elif len(group) == 2:
		return 1
	elif len(group) == 3:
		return 2
	elif len(group) == 4:
		return 4
	elif len(group) == 5:
		return 7
	else:
		print("ERROR: I can't cheat the calculation for that number")



def main(input_file):

	adapters = []

	with open(input_file, "r") as fp:
		
		text = fp.readlines()	

	adapters = sorted(list(map(int, text)))
	
	groups = divvy(adapters)

	groups[0] = [0] + groups[0]

	combinations = 1

	for group in groups:
		print(group)
		combinations *= combinatorics(group) 

	print(f"The number of possible adapter combinations is {combinations}")


	

if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
