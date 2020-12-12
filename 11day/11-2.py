#!/usr/bin/python3

import sys

day = 11 #Advent of Code day


def print_seats(seats):
	for line in seats:
		print("".join(line))


# Sometimes, it's not worth it to be clever
def check_around(seats, x, y):

	count = 0
	syms = ('#','L')


	i = x-1
	while i > -1:
		if seats[y][i] is not '.':
			if seats[y][i] == '#':
				count += 1
			break
		else:
			i -= 1

	j = y-1
	while j > -1:
		if seats[j][x] is not '.':
			if seats[j][x] == '#':
				count += 1
			break
		else:
			j -= 1

	i = x+1
	while i < len(seats[y]):
		if seats[y][i] is not '.':
			if seats[y][i] == '#':
				count += 1
			break
		else:
			i += 1

	j = y+1
	while j < len(seats):
		if seats[j][x] is not '.':
			if seats[j][x] == '#':
				count += 1
			break
		else:
			j += 1

	i = x-1
	j = y-1
	while i > -1 and j > -1:
		if seats[j][i] is not '.':
			if seats[j][i] == '#':
				count += 1
			break
		else:
			i -= 1
			j -= 1

	i = x+1
	j = y-1
	while i < len(seats[y]) and j > -1:
		if seats[j][i] is not '.':
			if seats[j][i] == '#':
				count += 1
			break
		else:
			i += 1
			j -= 1

	i = x+1
	j = y+1
	while i < len(seats[y]) and j < len(seats):
		if seats[j][i] is not '.':
			if seats[j][i] == '#':
				count += 1
			break
		else:
			i += 1
			j += 1

	i = x-1
	j = y+1
	while i > -1 and j < len(seats):
		if seats[j][i] is not '.':
			if seats[j][i] == '#':
				count += 1
			break
		else:
			i -= 1
			j += 1

	return count



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

			if 	 around >= 5 and seats[y][x] == '#':
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
