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

	#Initial floor pattern
	for t in data:

		dirs = dir_pat.findall(t)
		cur = (0,0,0)

		for d in dirs:
			cur = floor.mv_adj(cur,d)

		flip = floor.flip(cur, 'W', 'B')

	for i in range( 100):

		print(f"Iteration {i}: {floor.count('B')} black tiles")
		flippers = []

		for h in sorted(floor):

			count = floor.count_adj(h, 'B')

			if   (floor[h] == 'B' and count not in (1,2)) or (floor[h] == 'W' and count == 2):
				flippers.append(h)

			elif floor[h] != 'B' and count == 0:
				floor.pop(h)


		for f in flippers:
			floor.flip(f, 'B', 'W')
	
	print(f"After 100 days there are {floor.count('B')} black tiles")



if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
