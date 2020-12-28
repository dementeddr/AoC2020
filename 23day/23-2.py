#!/usr/bin/python3

import sys

day = 23 #Advent of Code day

rounds = 10000000
size = 1000000
print_inc = 500000



def main(input_file):

	data = ''
	cups = [0 for i in range(10)]

	with open(input_file, "r") as fp:
		data = list(map(int, fp.read()[:-1])) + [10]

	for i,num in enumerate(data[:-1]):
		cups[num] = data[i+1] 

	cups += [i+1 for i in range(10, size)] + [1]
	cur = 1

	for i in range(rounds):

		trey = [cups[cur], cups[cups[cur]], cups[cups[cups[cur]]]]
		dest = 0

		for j in range(1,5):
			dest = (cur-j) % len(cups)
			if dest != 0 and dest not in trey:
				break

		cnext = cups[trey[2]]
		dnext = cups[dest]
		
		cups[dest] = trey[0]
		cups[trey[2]] = dnext
		cups[cur] = cnext
		cur = cnext

		if i % print_inc == 0:
			print(f"{i:>8}: trey={trey}, 2after1=[{cups[1]},{cups[cups[1]]}]")
	
	print(f"Product of the 2 cups following 1: {cups[1]} * {cups[cups[1]]} = {cups[1] * cups[cups[1]]}")



if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
