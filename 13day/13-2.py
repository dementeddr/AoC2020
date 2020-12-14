#!/usr/bin/python3

import sys
import math
from functools import reduce

day = 13 #Advent of Code day



def main(input_file):

	buses = []
	sched = {}
	xs = 0

	with open(input_file, "r") as fp:
		fp.readline()
		buses = fp.readline().split(',')

	for bus in buses:
			
		xs += 1
		
		if bus == 'x':
			continue
		else:
			ibus = int(bus)
			sched[ibus] = xs % ibus

	print(sched)
	
	sched_s = sorted(sched.keys())

	upper_bound = reduce(lambda a, b: a*b, sched_s)
	print(upper_bound)

	interval = 1
	timestamp = 1

	for bus in sched_s:
		 while (timestamp + sched[bus]) % bus != 0:
		 	timestamp += interval

		 interval *= bus

	timestamp += 1 #I don't know why.

	print(f"You'll have to wait until {timestamp} to catch the right bus.")
	


if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
