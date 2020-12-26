#!/usr/bin/python3

import sys
import copy

day = 22 #Advent of Code day



def score(cards):

	points = 0

	for i, card in enumerate(reversed(cards)):
		points += (i+1) * card

	return points



def shaharazad(mine, crab):

states = set()

	while len(mine) > 0 and len(crab) > 0:
	
		state = (tuple(mine), tuple(crab)) 

		if state in states:
			print("The Wheel of Time turns, and Ages come and pass.")
			return 0
		else:
			states.add(state)
	
		m = mine.pop(0)
		c = crab.pop(0)
		winner = -1

		if   m <= len(mine) and c <= len(crab):
			winner = shaharazad(copy.deepcopy(mine[0:m]), copy.deepcopy(crab[0:c]))
		elif m > c:
			winner = 0
		elif m < c:
			winner = 1
		else:
			print(f"ERROR: The crab is cheating: {m} {c}")

		if winner == 0:
			mine.append(m)
			mine.append(c)
		elif winner == 1:	
			crab.append(c)
			crab.append(m)
		else:
			print(f"ERROR: There is no winner this round. {winner}")

	
	if len(mine) > 0:
		return 0
	elif len(crab) > 0:
		return 1
	else:
		print(f"ERROR: Recursion doesn't work that way! {mine} {crab}")
	


def main(input_file):

	crab = ''
	mine = ''

	with open(input_file, "r") as fp:
		mine, crab = fp.read().split('\n\n')

	mine = list(map(int,mine.split('\n')[1:]))
	crab = list(map(int,crab.split('\n')[1:-1]))
		
	winner = shaharazad(mine, crab)
	points = 0

	if winner == 0:
		print(f"You beat the voidbringer!  {mine}")
		points = score(mine)

	elif winner == 1:
		print(f"Turns out Adonalsium IS a crab...  {crab}")
		points = score(crab)
	else:
		print(f"ERROR: THERE CAN ONLY BE ONE! CRABLANDER!")

	print(f"Final score: {points}")
	


if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
