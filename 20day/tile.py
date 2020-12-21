#!/usr/bin/python3

class Tile():

	def hash_edge(string):

		if isinstance(string, list):
			string = ''.join(string)

		return int(string.replace('#', '1').replace('.','0'), 2)


	def __init__(self, data):
		
		if data == '':
			return None

		text = data.split('\n')
		self.name = int(text[0][5:-1])
		self.data = text[1:]
		self.isoriented = False

		N = self.data[0]
		E = ''.join(list(map(lambda l: l[0], self.data)))
		S = self.data[-1]
		W = ''.join(list(map(lambda l: l[-1], self.data)))

		#[N, E, S, W, Wf, Sf, Ef, Nf]
		self.edges = [None for i in range(8)]

		self.edges[0] = Tile.hash_edge(N)
		self.edges[1] = Tile.hash_edge(E)
		self.edges[2] = Tile.hash_edge(S)
		self.edges[3] = Tile.hash_edge(W)

		self.edges[4] = Tile.hash_edge(W[::-1])
		self.edges[5] = Tile.hash_edge(S[::-1])
		self.edges[6] = Tile.hash_edge(E[::-1])
		self.edges[7] = Tile.hash_edge(N[::-1])


	def __str__(self):
		return '\n'.join(self.data)
