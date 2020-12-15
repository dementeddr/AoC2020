#!/usr/bin/python3

import sys

day = 15 #Advent of Code day
target = 2020


def main(input_file):

	with open(input_file, "r") as fp:
		data = list(map(int, fp.readline().split(',')))

	nums = [0 for i in range(target)]
	print(data)

	for i in range(len(data)):
		nums[data[i]] = i+1
		print(f"{i+1:>4}: {data[i]}")

	prev = data[-1]

	for i in range(len(data), target):

		# Speak 0!
		if nums[prev] == 0:
			nums[prev] = i
			prev = 0
		else:
			prev2 = nums[prev]
			nums[prev] = i
			prev = i - prev2

		print(f"{i+1:>4}: {prev}")

	print(f"Spoken number number {target} is {prev}")



if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
