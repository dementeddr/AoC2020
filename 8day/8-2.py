#!/usr/bin/python3

import sys

day = 8 #Advent of Code day

def main(input_file):

	insts = []

	with open(input_file, "r") as fp:
		insts = fp.readlines()

	touched = [None for i in range(len(insts))]
	acc = 0
	ic = 0
	found = False

	while touched[ic] is None:

		touched[ic] = ic
		op, arg = insts[ic].split(' ')
		arg = int(arg)

		if op in ("nop", "jmp"): #branch
			b_touch = touched.copy()
			b_ic = ic
			b_acc = acc
			b_op = op
			b_arg = arg

			if 	 op == "nop":
				b_op = "jmp"
			elif op == "jmp":
				b_op = "nop"
			else:
				print(f"ERROR: Should not be branching on {op}")
		
			b_touch[b_ic] = None

			while b_touch[b_ic] is None:
				b_touch[b_ic] = b_ic

				if	 b_op == "acc":
					b_ic += 1
					b_acc += b_arg

				elif b_op == "nop":
					b_ic += 1

				elif b_op == "jmp":
					b_ic += b_arg

				else:
					print(f"ERROR, bad branch op: {b_op}")

				if b_ic >= len(insts):
					print(f"Correct instruction fixed. ACC = {b_acc}")
					found = True
					break

				b_op, b_arg = insts[b_ic].split(' ')
				b_arg = int(b_arg)

			if   found:
				print("Done")
				break
		
		if	 op == "nop":
			ic += 1
		elif op == "jmp":
			ic += arg
		elif op == "acc":
			acc += arg
			ic += 1
		else:
			print(f"ERROR, bad op: {op}")

	if not found:
		print("Boot sequence has looped.")



if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
