#!/usr/bin/python3

import sys

day = 13 #Advent of Code day

def main(input_file):

	departure = 0
	buses = []

	with open(input_file, "r") as fp:
		departure = int(fp.readline())
		buses = fp.readline().split(',')

	leave_time = departure * 2
	leave_bus = 0

	print(departure)

	for bus in buses:
		
		if bus == 'x':
			continue
		else:
			bus = int(bus)

		print(bus)

		time = 0

		while time < departure:
			time += bus

		if time < leave_time:
			leave_time = time
			leave_bus = bus

		print(f"\t{leave_time} - {leave_bus}")

	print(leave_bus * (leave_time - departure))



if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
