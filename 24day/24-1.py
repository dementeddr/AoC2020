#!/usr/bin/python3

import sys
import re
from hexgrid import HexGrid

day = 24 #Advent of Code day



def main(input_file):

	data = []
	floor = HexGrid('W')
	dir_pat = re.compile(r"e|se|sw|w|nw|ne")

	with open(input_file, "r") as fp:
		data = fp.read().split('\n')[:-1]

	for t in data:

		print(t)
		dirs = dir_pat.findall(t)

		cur = (0,0,0)

		for d in dirs:
			cur = floor.mv_adj(cur,d)
			#print(f"{d}: {cur}")

		flip = floor.flip(cur, 'W', 'B')

		print(f"Flipped {cur} to {flip}")

	print(f"The number of black tiles in the floor is {floor.count('B')}")



if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
