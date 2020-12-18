#!/usr/bin/python3

import sys

day = 17 #Advent of Code day

def print_pocket(pocket):
	i = 0
	for zz in pocket:
		for yy in zz:
			out = ''
			for xx in yy:
				out += xx
			print(out)
		print('='*len(zz) + f" {i}")
		i+=1


#coords are x, y, z
def check_around(pocket, coords=[10,10,10]):
	
	assert len(coords) == 3

	unwrap = ''

	for z in range(-1,2):
		for y in range(-1,2):
			for x in range(-1,2):
				#print(f"{z:>2} {y:>2} {x:>2}  +  {coords[2]} {coords[1]} {coords[0]}  =  {coords[2]+z:>2} {coords[1]+y:>2} {coords[0]+x:>2}")
				unwrap += pocket[coords[2]+z][coords[1]+y][coords[0]+x]
				
	unwrap = unwrap[:13] + unwrap[14:] #Exclude the central point
	return unwrap.count('#') + unwrap.count('V')
	


def iterate(pocket):
	
	for z in range(1, len(pocket)-1):
		for y in range(1, len(pocket[z])-1):
			for x in range(1, len(pocket[z][y])-1):
				energy = check_around(pocket, [x, y, z])
				status = pocket[z][y][x]
				#print(f"{x:>2} {y:>2} {z:>2}: {pocket[z][y][x]} - {energy}")
					
				if 	 status == '#' and energy not in (2, 3):
					pocket[z][y][x] = 'V'
				elif status == '.' and energy == 3:
					pocket[z][y][x] = '^'
				
	
	for z in range(len(pocket)):
		for y in range(len(pocket[z])):
			for x in range(len(pocket[z][y])):
				if 	 pocket[z][y][x] == 'V':
					pocket[z][y][x] = '.'
				elif pocket[z][y][x] == '^':
					pocket[z][y][x] = '#'
				else:
					continue



def main(input_file):

	pocket = [[['.' for x in range(22)] for y in range(22)] for z in range(22)]
	data = ''

	with open(input_file, "r") as fp:
		data = fp.read().split('\n')

	for y in range(len(data)):
		
		for x in range(len(data[y])):

			pocket[11][7+y][7+x] = data[y][x]


	for i in range(6):
		iterate(pocket)

	print_pocket(pocket)
	
	count = 0

	for zz in pocket:
		for yy in zz:
			for xx in yy:
				if xx == '#':
					count += 1

	print(f"The number of active cubes in the pocket dimension is {count}")



if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
