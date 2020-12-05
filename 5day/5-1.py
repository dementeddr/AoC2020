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

highest_id = 0

with open(input_file, "r") as fp:

	for seat in fp:
		
		ids = [i for i in range(1024)]

		for c in seat[:-1]:

			ids = halve(ids, c)

		if ids[0] > highest_id:
			highest_id = ids[0]

print(f"The highest id seat around is {highest_id}")
			

