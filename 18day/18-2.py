#!/usr/bin/python3

import sys

day = 18 #Advent of Code day



def find_close(eq, op):
	parens = ['(']
	for c in range(op+1, len(eq)):
		if eq[c] == '(':
			parens.append('(')
		elif eq[c] == ')':
			parens.pop()

		if len(parens) == 0:
			return c



def process(tokens):

	for t in range(len(tokens)):
		if isinstance(tokens[t], list):
			tokens[t] = process(tokens[t])

	ix = 1

	while ix < len(tokens):
		if tokens[ix] == '+':
			tokens = tokens[:ix-1] + [tokens[ix-1] + tokens[ix+1]] + tokens[ix+2:]
		else:
			ix += 1

	ix = 1
	while len(tokens) > 1:
		if tokens[ix] == '*':
			tokens = tokens[:ix-1] + [tokens[ix-1] * tokens[ix+1]] + tokens[ix+2:]
		else:
			ix += 1

	return tokens[0]



def lex(eq_text):

	ix = 0
	tokens = []
	
	#print(f"lexing: {''.join(eq_text)}")

	while ix < len(eq_text):
		c = eq_text[ix]

		if	 c == '(':
			close = find_close(eq_text, ix)
			tokens.append(lex(eq_text[ix+1:close]))
			ix = close

		elif c.isdigit():
			tokens.append(int(c))

		elif c in ('+', '*'):
			tokens.append(c)

		else:
			print(f"Unknown element: {c}")

		ix += 1

	#print(f"Lex result: {tokens}")

	return tokens



def main(input_file):

	total = 0
	data = ''

	with open(input_file, "r") as fp:
		data = fp.readlines()

	for line in data:
		line = line.replace('(', '( ').replace(')', ' )').split()
		tokens = lex(line)
		total += process(tokens)
		#print(f"Running Total: {total}")

	print(f"The sum of the listed equations is {total}")



if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
