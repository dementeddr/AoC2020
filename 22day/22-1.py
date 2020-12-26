#!/usr/bin/python3

import sys
from collections import deque

day = 22 #Advent of Code day

def main(input_file):

	crab = ''
	mine = ''

	with open(input_file, "r") as fp:
		mine, crab = fp.read().split('\n\n')

	mine = deque(list(map(int,mine.split('\n')[1:])))
	crab = deque(list(map(int,crab.split('\n')[1:-1])))
		
	while len(mine) > 0 and len(crab) > 0:

		m = mine.popleft()
		c = crab.popleft()
		
		if m > c:
			mine.append(m)
			mine.append(c)
		elif m < c:
			crab.append(c)
			crab.append(m)
		else:
			print(f"ERROR: The crab is cheating: {m} {c}")

	winner = None
	
	if len(mine) > 0:
		print(f"You beat the voidbringer!  {mine}")
		winner = mine
	elif len(crab) > 0:
		print(f"Turns out Adonalsium IS a crab...  {crab}")
		winner = crab
	else:
		print(f"ERROR: THERE CAN ONLY BE ONE! CRABLANDER!")

	score = 0
	
	for i, card in enumerate(reversed(winner)):
		score += (i+1) * card

	print(f"Final score: {score}")
	


if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
