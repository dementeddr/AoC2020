#!/usr/bin/python3

import sys
import xmas


day = 9 #Advent of Code day


def find_min_max(array):
	
	the_min = sys.maxsize
	the_max = 0

	for el in array:
		if el > the_max:
			the_max = el
		if el < the_min:
			the_min = el

	return (the_min, the_max)



def main(input_file):

	invalid_num = 675280050
	input_data = []

	with open(input_file, "r") as fp:
		for line in fp:
			input_data.append(int(line))
			if input_data[-1] == invalid_num:
				break

	for i in range(len(input_data)):

		run_sum = 0

		for j in range(i,len(input_data)):
			run_sum += input_data[j]
			if run_sum == invalid_num:
				endpoints = find_min_max(input_data[i:j])
				print(f"The min max of the contiguous sum is {endpoints}, which sum to {endpoints[0] + endpoints[1]}")
				exit()

			elif run_sum > invalid_num:
				break

			

if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
