#!/usr/bin/python3

import sys

day = 25 #Advent of Code day

mod = 20201227



def calc_loop(sub, pub):
	
	loop = 0
	val = 1

	while val != pub:
		val = (val * sub) % mod
		loop += 1

	return loop



def calc_key(pub, loop):
	
	val = 1

	for i in range(loop):
		val = (val * pub) % mod

	return val



def main(input_file):

	pub_c = ''
	pub_d = ''

	with open(input_file, "r") as fp:
		pub_c = int(fp.readline())
		pub_d = int(fp.readline())

	loop_c = calc_loop(7, pub_c)
	print(f"Card loop size {loop_c}")
	loop_d = calc_loop(7, pub_d)
	print(f"Door loop size {loop_d}")

	key_c = calc_key(pub_d, loop_c)	
	key_d = calc_key(pub_c, loop_d)	
	
	print(f"The encryption key is {key_c}. Or is it {key_d}...?")
	


if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
