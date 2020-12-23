#!/usr/bin/python3

import sys
from collections import defaultdict
from tile import Tile

day = 20 #Advent of Code day

def main(input_file):

	data = ''
	tiles = {}
	all_edges = defaultdict(lambda : [])

	with open(input_file, "r") as fp:
		data = fp.read().split("\n\n")

	for t in data[:-1]:
		obj = Tile(t)
		tiles[obj.name] = obj

		for e in obj.edges:
			all_edges[e].append(obj.name)
	
	corner_pieces = [] #defaultdict(lambda : 0)
	total = 1

	for t in tiles:
		outer_edges = 0
		for e in tiles[t].edges:
			if len(all_edges[e]) == 1:
				outer_edges += 1

		if outer_edges == 4:
			corner_pieces.append(t)
			total *= t

	print(corner_pieces)
	print(f"The product of the ids of all the corner pieces is {total}")



if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
