#!/usr/bin/python3

import sys
import re

day = 16 #Advent of Code day

def check_num(num, field):

	return (num >= field[0] and num <= field[1]) or (num >= field[2] and num <= field[3])



def isValid(ticket, fields):

	for num in ticket:
		
		isVal = False

		for f in fields:

			if check_num(num, fields[f]):
				isVal = True
				break

		if not isVal:
			return False

	return True



def non_field_check(num, fields):

	invals = set()

	for f in fields.keys():

		if not check_num(num, fields[f]):
			invals.update([f])

	return invals



def cross_check(tickets, fields):

	possibles = [set(fields.keys()) for i in range(len(tickets[0]))]

	for i in range(len(tickets[0])):

		for j in range(len(tickets)):

			temp = non_field_check(tickets[j][i], fields)
			possibles[i] -= temp
			
			if len(possibles[i]) == 1:
				break

			elif len(possibles[i]) <= 0:
				print("shit")

	return possibles



def remove_possibility(possibles, field):

	for i in range(len(possibles)):
		possibles[i].difference_update(field)

	return possibles



def main(input_file):

	field_re = re.compile(f"([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)")

	with open(input_file, "r") as fp:
		data = fp.read().split('\n\n')

	field_str = data[0].split('\n')
	my_ticket = list(map(int, data[1].split('\n')[1].split(',')))
	tickets = data[2].split('\n')[1:-1]
	valid_ticks = []
	fields = {}
	
	for field in field_str:
		f_re = field_re.match(field)
		fields[f_re.group(1)] = list(map(int, f_re.groups()[1:]))

	for tic in tickets:
		val = list(map(int, tic.split(',')))
		if isValid(val, fields):
			valid_ticks.append(val)
	
	possibles = cross_check(valid_ticks, fields)
	field_order = ['' for i in range(len(fields))]
	notDone = True

	while notDone:

		notDone = False

		for i in range(len(possibles)):

			if possibles[i] is not None and len(possibles[i]) == 1:

				field_order[i] = list(possibles[i])[0]
				possibles = remove_possibility(possibles, field_order)
				notDone = True

	print(field_order)

	total = 1

	for i in range(len(my_ticket)):
		if field_order[i].count("departure") >= 1:
			total *= my_ticket[i]

	print(f"The product of your departure fields is {total}")



if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
