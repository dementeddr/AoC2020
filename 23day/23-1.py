#!/usr/bin/python3

import sys

day = 23 #Advent of Code day

def main(input_file):

	cups = ''

	with open(input_file, "r") as fp:
		
		cups = list(map(int, fp.read()[:-1]))

	print(cups)

	for i in range(100):

		trey = [cups.pop(1), cups.pop(1), cups.pop(1)]

		for j in range(1,9):

			dest = (cups[0] - j) % 10

			if dest in cups:
				ins = cups.index(dest)+1
				cups = cups[1:ins] + trey + cups[ins:] + [cups[0]]
				break

		print(f"{i:>3}: {cups}")


	ind = cups.index(1)
	out = ''.join([str(num) for num in cups[ind+1:] + cups[:ind]])
	print(f"Post-1 cup order: {out}")



if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
