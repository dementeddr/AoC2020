#!/usr/bin/python3

import sys

day = 18 #Advent of Code day

def operate(arg1, arg2, math):

	#print(f"{arg1} {arg2} {math}   {list(map(type,[arg1, arg2, math]))}")

	if math == '+':
		return arg1 + arg2
	elif math == '*':
		return arg1 * arg2


def find_close(eq, op):
	parens = ['(']
	for c in range(op+1, len(eq)):
		if eq[c] == '(':
			parens.append('(')
		elif eq[c] == ')':
			parens.pop()

		if len(parens) == 0:
			return c


def parse(eq):

	op = 0
	token = None
	math = ''

	print(f"Parsing: '{eq}'")

	while op < len(eq):
		
		if 	 eq[op] == '(':
			close = find_close(eq, op)
			res = parse(eq[op+1:close])
			
			if token is None:
				token = res
			else:
				token = operate(token, res, math)
			op = close

		elif eq[op].isdigit():
			if token is None:
				token = int(eq[op])
			else:
				token = operate(token, int(eq[op]), math)	
			
		elif eq[op] in ('+','*'):
			math = eq[op]

		op+=1
	
	return token

	

def main(input_file):

	total = 0
	data = ''

	with open(input_file, "r") as fp:
		data = fp.readlines()

	for line in data:
		total += parse(line.replace(' ', ''))
		print(f"Total: {total}")

	print(total)

	
		


if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
