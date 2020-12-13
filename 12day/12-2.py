#!/usr/bin/python3

import sys

day = 12 #Advent of Code day


def main(input_file):

	x = 0
	y = 0
	wx = 10
	wy = 1

	with open(input_file, "r") as fp:
		for line in fp:
			act = line[0]
			num = int(line[1:])

			if	 act == 'N':
				wy += num
			elif act == 'S':
				wy -= num
			elif act == 'E':
				wx += num
			elif act == 'W':
				wx -= num
			
			elif act == 'L':
				for i in range(num // 90):
					temp = wx
					wx = -wy
					wy = temp

			elif act == 'R':
				for i in range(num // 90):
					temp = wx
					wx = wy
					wy = -temp

			elif act == 'F':
				x += wx * num
				y += wy * num

			else:
				print("ERROR: You dun fucked up. {act}")

	print(f"Manhatten says {x} + {y} = {abs(x) + abs(y)}")



if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
