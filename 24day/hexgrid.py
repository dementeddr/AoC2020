#!/usr/bin/python3

class HexGrid():

	dirs = {
		'e' : (1, -1, 0),
		'se': (0, -1, 1),
		'sw': (-1, 0, 1),
		'w' : (-1, 1, 0),
		'nw': (0, 1, -1),
		'ne': (1, 0, -1),
	}

	def validate_key(key):
		
		if isinstance(key, list):
			key = tuple(key)

		if not isinstance(key, tuple):
			raise KeyError(f"HexGrid key must be a list or tuple, not {type(key)}")

		if len(key) != 3:
			raise KeyError(f"HexGrid key must have length 3, not {len(key)}")
		
		return key


		
	def mv_adj(self, key, direction):

		key = HexGrid.validate_key(key)

		if direction not in HexGrid.dirs:
			raise ValueError(f"'{direction}' is not a valid hex direction")

		d = HexGrid.dirs[direction]
		
		return tuple(map(lambda c: d[c] + key[c], range(3)))



	def adj_keys(self, key):

		key = HexGrid.validate_key(key)
		ret = []

		for d in HexGrid.dirs:
			ret.append(self.mv_adj(key, d))

		return ret



	def count(self, value):

		return len(tuple(filter(lambda v: v==value, self.grid.values())))



	def is_real(self, key):

		key = HexGrid.validate_key(key)
		return key in self.grid



	def flip(self, key, v1, v2):

		key = HexGrid.validate_key(key)

		#if key not in self.grid:
		#	self[key] = self.default

		if   self[key] == v1:
			self[key] = v2
			return v2

		elif self[key] == v2:
			self[key] = v1
			return v1

		else:
			raise ValueError(f"Value at HexGrid[{key}] is {self.grid[key]}, not {v1} or {v2}")



	def get_adj(self, key, direction):
	
		return self.grid[self.mv_adj(key, direction)]


	
	def count_adj(self, key, value):

		key = HexGrid.validate_key(key)

		return len(tuple(filter(lambda d: self[d] == value, self.adj_keys(key))))	



	def __getitem__(self, key):

		key = HexGrid.validate_key(key)

		if key in self.grid:
			return self.grid[key]
		else:
			return self.default



	def __setitem__(self, key, value):

		key = HexGrid.validate_key(key)
		self.grid[key] = value

		for d in self.adj_keys(key):
			if d not in self.grid:
				self.grid[d] = self.default



	def __iter__(self):

		return self.grid.__iter__()



	def __init__(self, default=None):

		self.grid = {(0,0,0):default}
		self.default = default


