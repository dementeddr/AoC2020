#!/usr/bin/python3

import sys

day = 12 #Advent of Code day

def change_dir(d, act, rot):
	
	if act == 'L':
		rot = -rot

	d = (d + rot) % 360

	return d
	

def main(input_file):

	x = 0
	y = 0
	d = 0 #East

	with open(input_file, "r") as fp:
		for line in fp:
			act = line[0]
			num = int(line[1:])

			if	 act == 'N':
				y += num
			elif act == 'S':
				y -= num
			elif act == 'E':
				x += num
			elif act == 'W':
				x -= num
			elif act == 'L':
				d = (d - num) % 360
			elif act == 'R':
				d = (d + num) % 360
			elif act == 'F':
				if 	 d == 0:
					x += num
				elif d == 90:
					y -= num
				elif d == 180:
					x -= num
				elif d == 270:
					y += num
				else:
					print("ERROR: what is this non-orthogonal bullshit? " + num)

			else:
				print("ERROR: You dun fucked up. {act}")

	print(f"Manhatten says {x} + {y} = {abs(x) + abs(y)}")



if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
