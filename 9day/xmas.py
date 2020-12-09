#!/usr/bin/python3

class XMAS():

	def __init__(self, preamble):
		self.size = len(preamble)
		self.data = preamble

		self.table = [[0 for i in range(self.size)] for j in range(self.size)]

		for y in range(self.size):
			for x in range(self.size):
				self.table[x][y] = -1 if x == y else self.data[x] + self.data[y]

	def increment(self, new_num):
		self.data.pop(0)
		self.data.append(new_num)

		self.table.pop(0)
		self.table.append([num + new_num for num in self.data])

		for i in range(self.size):
			self.table[i].pop(0)
			self.table[i].append(self.data[i] + new_num)

		self.table[-1][-1] = -1 #eliminate sums of numbers + themselves

	def check_number(self, num):
		
		for line in self.table:
			for cell in line:
				if num == cell:
					return True

		return False

	
	def str_line(line, pad=4):

		ret = ""

		for num in line:
			ret += f"{num:>{pad}}, "

		return ret


	def __str__(self):
		
		ret = ""

		for line in self.table:
			ret += XMAS.str_line(line) + '\n' 

		return ret

