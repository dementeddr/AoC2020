#!/usr/bin/python3

import sys
import re
from collections import defaultdict
from tile import Tile

day = 20 #Advent of Code day


def find_piece(pieces, target_edge, target_orient):

	#print(f"Finding piece with edge {target_edge} in set with size {len(pieces)}")

	for i, piece in enumerate(pieces):
		#print(f"Checking tile {piece.name}\n{piece.edges}")
		index = piece.find_edge(target_edge)
		#print(piece)

		if index != -1:

			found = pieces.pop(i)
			#print(f"Found: {found.name}. Orienting: {index} => {target_orient}")
			found.orient(index, target_orient)

			#print(found)
			#print(f"{'='*30}")
			return found
	
	print("ERROR: No matching piece found")
	return None



def assemble_row(row, target_edge, match_edge, inner_pieces, end_pieces):

	for j in range(1, len(row)-1):
		row[j] = find_piece(inner_pieces, row[j-1].edges[target_edge], match_edge)
	
	#print(end_pieces)

	row[-1] = find_piece(end_pieces, row[-2].edges[target_edge], match_edge)

	return row


def assemble_puzzle(data):

	tiles = {}
	all_edges = defaultdict(lambda : [])
	
	#Turn input into a dictionary of tiles
	for t in data[:-1]:
		obj = Tile(t)
		tiles[obj.name] = obj

		for e in obj.edges:
			all_edges[e].append(obj.name)
	
	#Find the corner and edge pieces
	corner_pieces = []
	edge_pieces = []
	inner_pieces = []
	total = 1

	for t in tiles:
		outer_edges = 0
		for e in tiles[t].edges:
			if len(all_edges[e]) == 1:
				outer_edges += 1

		if outer_edges == 4:
			corner_pieces.append(tiles[t])
		elif outer_edges == 2:
			edge_pieces.append(tiles[t])
		else:
			inner_pieces.append(tiles[t])

	#print(corner_pieces)

	#Start the puzzle
	puzzle = [None for j in range(12)]
	puzzle[0] = corner_pieces.pop(0)
	#print(puzzle[0])
	#print(puzzle[0].edges)
	puzzle[0].orient(3,1) #I'm cheating here because I figured out how the corner should be oriented by eyeball and writing the code wasn't worth the trouble.
	#print(puzzle[0])
	#print(puzzle[0].edges)
	
	#Assemble the west side
	puzzle = assemble_row(puzzle, 2, 0, edge_pieces, corner_pieces)
	#print(f"{'$'*40} Starting top assembly")
	
	#Assemble the north side
	puzzle[0] = [puzzle[0]] + [None for i in range(11)]
	puzzle[0] = assemble_row(puzzle[0], 1, 3, edge_pieces, corner_pieces)
	#print(f"{'$'*40} Starting inside assembly")
	
	#Assemble the inside
	for j in range(1, len(puzzle)-1):
		#print(f"\t{'$'*20} Beginning Row {j}")
		row = [puzzle[j]] + [None for i in range(11)]
		puzzle[j] = assemble_row(row, 1, 3, inner_pieces, edge_pieces)

	#Assemble the south side
	puzzle[-1] = [puzzle[-1]] + [None for i in range(11)]
	puzzle[-1] = assemble_row(puzzle[-1], 1, 3, edge_pieces, corner_pieces)

	return puzzle



def create_picture(puzzle):
	
	picture = []

	for line in puzzle:
		
		for j in range(8):
			scanline = ''.join(list(map(lambda x : x.data[j], line)))
			#print(scanline)
			picture.append(scanline)

	return picture



def find_monsters(pic):

	count = 0
	w = (8*12) + 1 - 18
	w2 = w + (8*12) + 2
	c2 = 0
	
	for i in range(19, len(pic[:-(w2+16)])): 
		if pic[i] != '#':
			continue
		c2 += 1

		monster = ''.join([
			pic[i],
			pic[i+w],
			pic[i+w+5],
			pic[i+w+6],
			pic[i+w+11],
			pic[i+w+12],
			pic[i+w+17],
			pic[i+w+18],
			pic[i+w+19],
			pic[i+w2],
			pic[i+w2+3],
			pic[i+w2+6],
			pic[i+w2+9],
			pic[i+w2+12],
			pic[i+w2+15]
		])

		#print(f"{i:>5}: {monster}")

		if monster.count('#') == 15:
			count += 1

		if False: #c2 == 23:
			pic2 = list(pic)
			out = [
				i,
				i+w,
				i+w+5,
				i+w+6,
				i+w+11,
				i+w+12,
				i+w+17,
				i+w+18,
				i+w+19,
				i+w2,
				i+w2+3,
				i+w2+6,
				i+w2+9,
				i+w2+12,
				i+w2+15
			]
			for c in out:
				pic2[c] = '0'

			print(''.join(pic2))

	return count
	


def main(input_file):

	data = ''
	#fuzzy_shape = re.compile(r"#.+\s.*#.{4}##.{4}##.{4}###.*\s.*(?:#..){6}")

	with open(input_file, "r") as fp:
		data = fp.read().split("\n\n")

	puzzle = assemble_puzzle(data)
	pic_file = create_picture(puzzle)
	
	pic_file.reverse()
	
	for i in range(3):
		pic_file = list(map(lambda t: ''.join(t), list(zip(*pic_file))))


	picture = '\n'.join(pic_file)
	monsters = find_monsters(picture)
	
	print(picture)
	print(f"#Monsters: {monsters}")

	roughness = picture.count('#') - (15*monsters)

	print(f"The roughness level of the seas is {roughness}, because you have to avoid {monsters} sea monsters")


if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
