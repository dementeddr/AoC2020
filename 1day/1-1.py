#!/usr/bin/python3

import heapq
import sys

input_file = "input-d1.txt"

if len(sys.argv) > 1:
	input_file = sys.argv[1]


def find_pair(sorted_list):

	for num in sorted_list:
		print(num)
		
		for compliment in reversed(sorted_list):
			if num + compliment == 2020:
				print(f"Today's matching numbers are: {num} and {compliment}")
				return (num, compliment)
			elif num + compliment < 2020:
				break

heap = []

with open(input_file, "r") as fp:
	
	for num in fp:
		#print(int(num))
		heapq.heappush(heap, int(num))

sorted_list = [heapq.heappop(heap) for i in range(len(heap))]

pair = find_pair(sorted_list)

print(f"The auditor says: {pair[0] * pair[1]}")

