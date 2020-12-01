#!/usr/bin/python3

import heapq
import sys

input_file = "input-d1.txt"

if len(sys.argv) > 1:
	input_file = sys.argv[1]


def find_triple(sorted_list):

	for num1 in sorted_list:

		for num2 in reversed(sorted_list):
			
			compliment = num1 + num2

			if compliment > 2020:
				continue

			for num3 in sorted_list:

				if num3 + compliment == 2020:
					print(f"Today's numbers are: {num1} {num2} {num3}")
					return (num1, num2, num3)
				elif num3 + compliment > 2020:
					break

heap = []

with open(input_file, "r") as fp:
	
	for num in fp:
		heapq.heappush(heap, int(num))

sorted_list = [heapq.heappop(heap) for i in range(len(heap))]

triple = find_triple(sorted_list)

print(f"The auditor says: {triple[0] * triple[1] * triple[2]}")

