#!/usr/bin/python3

class Tile():

	FLIPPED_INDEX = {
		0 : 5,
		1 : 6,
		2 : 7,
		3 : 4,
		4 : 3,
		5 : 0,
		6 : 1,
		7 : 2,
		-1:-1,
	}

	def hash_edge(string):
		if isinstance(string, list):
			string = ''.join(string)

		return int(string.replace('#', '1').replace('.','0'), 2)


	def find_edge(self, target_edge):
		#print(f"Checking edges {self.edges}")
		for i in range(len(self.edges)):
			if self.edges[i] == target_edge:
				return i

		return -1


	def flip(self, index=-1):
		self.data.reverse()
		new_edges = [-1 for i in range(len(self.edges))]
		
		for i in range(len(self.edges)):
			new_edges[i] = self.edges[Tile.FLIPPED_INDEX[i]]
		
		self.edges = new_edges
		return Tile.FLIPPED_INDEX[index]


	# clocks = num rotations clockwise
	def rotate(self, clocks=1):

		#print(f"\tRotating {clocks} times")

		for r in range(clocks):
			N = self.edges.pop(3)
			Nf = self.edges.pop(3)
			self.edges.insert(0,N)
			self.edges.insert(7,Nf)
			
			#Magical matrix rotator I copied from SO
			self.data = list(map(lambda t: ''.join(t), list(zip(*self.data[::-1]))))



	def orient(self, index, target=3):
		#print(f"\tOrienting {index} => {target}")	
		true_index = 7 - index
		index1 = index
		if (true_index > 3) != (target > 3):
			true_index = self.flip(true_index)
			#print(f"\tFlipping {index1} => {index}")

		if true_index != target:
			self.rotate(((4-true_index) + target) % 4)

		self.isoriented = True



	def __init__(self, data):
		
		if data == '':
			return None

		text = data.split('\n')
		self.name = int(text[0][5:-1])
		self.data = text[1:]
		self.isoriented = False

		N = self.data[0]
		E = ''.join(list(map(lambda l: l[-1], self.data)))
		S = self.data[-1]
		W = ''.join(list(map(lambda l: l[0], self.data)))

		#[N, E, S, W, Wf, Sf, Ef, Nf]
		self.edges = [None for i in range(8)]

		self.edges[0] = Tile.hash_edge(N)
		self.edges[1] = Tile.hash_edge(E)
		self.edges[2] = Tile.hash_edge(S[::-1])
		self.edges[3] = Tile.hash_edge(W[::-1])

		self.edges[4] = Tile.hash_edge(W)
		self.edges[5] = Tile.hash_edge(S)
		self.edges[6] = Tile.hash_edge(E[::-1])
		self.edges[7] = Tile.hash_edge(N[::-1])

		self.data = list(map(lambda l: l[1:-1], self.data[1:-1]))



	def __str__(self):
		return '|' + '\n|'.join(self.data)
