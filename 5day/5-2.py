#!/usr/bin/python3

import sys

input_file = "input-d5.py"

if len(sys.argv) > 1:
	input_file = sys.argv[1]


def halve(array, c):
	half = ""
	#print(f"{c} - {array}")

	if 	 c in ('F','L'):
		half = array[:len(array)//2]
	elif c in ('B','R'):
		half = array[len(array)//2:]
	else:
		print("You dun fucked up.")
		exit()

	return half


open_seats = [i for i in range(1024)]

with open(input_file, "r") as fp:

	for seat in fp:
		
		ids = [i for i in range(1024)]

		for c in seat[:-1]:

			ids = halve(ids, c)

		open_seats[ids[0]] = None


for seat in open_seats:

	if seat is not None and open_seats[seat+1] is None and open_seats[seat-1] is None:
		print(f"Your seat id is {seat}")
	
