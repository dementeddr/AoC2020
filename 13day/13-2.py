#!/usr/bin/python3

import sys
import math

day = 13 #Advent of Code day


def criteria_check(sched, sched_s, timestamp):
	for bus in sched_s:
		if (timestamp + sched[bus]) % bus != 0:
			return False

	return True


def main(input_file):

	departure = 0
	buses = []
	sched = {}
	xs = 0

	with open(input_file, "r") as fp:
		departure = int(fp.readline())
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
	sched_s.reverse()
	min1 = sched_s[0]
	min2 = sched_s[1]

	iteration = 1
	interval = 1
	upper_bound = 1

	for bus in sched_s:
		diff = bus- (bus - sched[bus])
		interval = abs(diff * interval) // math.gcd(interval, diff)
		upper_bound *= bus
		print(interval)

	timestamp = interval

	while timestamp < upper_bound:
		print(timestamp)
		if criteria_check(sched, sched_s, timestamp):
			break
		else:
			timestamp += interval


	print(f"You'll have to wait until {timestamp} to catch the right bus.")
	


if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
