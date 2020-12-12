#!/usr/bin/python3

import sys

day = 11 #Advent of Code day


def print_seats(seats):
	for line in seats:
		print("".join(line))



def check_around(seats, x, y):

	around  = seats[y-1][x-1:x+2] + [seats[y][x-1]] + [seats[y][x+1] ]+ seats[y+1][x-1:x+2]
	return around.count('#')



def apply_changes(seats, changes):

	changed = False

	for y in range(len(seats)):
		for x in range(len(seats[y])):
			if changes[y][x] in ('#','L'):
				seats[y][x] = changes[y][x]
				changed = True

	return changed



def iterate(seats):

	changes = [[None for x in seats[0]] for y in seats]

	for y in range(1, len(seats)-1):
		for x in range(1, len(seats[y]) -1):

			around = check_around(seats, x, y)

			if 	 around >= 4 and seats[y][x] == '#':
				changes[y][x] = 'L'
			elif around == 0 and seats[y][x] == 'L':
				changes[y][x] = '#'


	return apply_changes(seats, changes)



def main(input_file):

	seats = []

	with open(input_file, "r") as fp:
		for line in fp:
			seats.append(list(line[:-1]))


	buff = ['.' for i in range(len(seats[0]))]
	seats = [buff] + seats + [buff]
	print_seats(seats)

	seats = list(map(lambda row: ['.'] + row + ['.'] , seats))

	while iterate(seats):
		print_seats(seats)

	full_seats = 0

	full_seats = sum(list(map(lambda row: row.count('#'), seats)))

	print(f"\nThe number of occupied seats is {full_seats}")
		


if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
