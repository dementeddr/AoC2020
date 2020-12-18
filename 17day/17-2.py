#!/usr/bin/python3

import sys

day = 17 #Advent of Code day

def print_pocket(pocket):
	i = 0
	for zz in pocket:
		for yy in zz:
			for xx in yy:
				out = ''
				for ww in xx:
					out += ww
				print(out)
			#print('='*len(zz) + f" {i}")
			i+=1


#coords are x, y, z
def check_around(pocket, coords=[10,10,10,10]):
	
	assert len(coords) == 4

	unwrap = ''

	for z in range(-1,2):
		for y in range(-1,2):
			for x in range(-1,2):
				for w in range(-1,2):
					#print(f"{z:>2} {y:>2} {x:>2}  +  {coords[2]} {coords[1]} {coords[0]}  =  {coords[2]+z:>2} {coords[1]+y:>2} {coords[0]+x:>2}")
					unwrap += pocket[coords[3]+z][coords[2]+y][coords[1]+x][coords[0]+w]
				
	unwrap = unwrap[:39] + unwrap[40:] #Exclude the central point
	return unwrap.count('#') + unwrap.count('V')
	


def iterate(pocket):
	
	for z in range(1, len(pocket)-1):
		for y in range(1, len(pocket[z])-1):
			for x in range(1, len(pocket[z][y])-1):
				for w in range(1, len(pocket[z][y][x])-1):
					energy = check_around(pocket, [w, x, y, z])
					status = pocket[z][y][x][w]
					#print(f"{x:>2} {y:>2} {z:>2}: {pocket[z][y][x]} - {energy}")
						
					if 	 status == '#' and energy not in (2, 3):
						pocket[z][y][x][w] = 'V'
					elif status == '.' and energy == 3:
						pocket[z][y][x][w] = '^'
	print("Evaluation complete. Changing state...")
	
	for z in range(len(pocket)):
		for y in range(len(pocket[z])):
			for x in range(len(pocket[z][y])):
				for w in range(len(pocket[z][y][x])):
					if 	 pocket[z][y][x][w] == 'V':
						pocket[z][y][x][w] = '.'
					elif pocket[z][y][x][w] == '^':
						pocket[z][y][x][w] = '#'
					else:
						continue



def main(input_file):

	pocket = [[[['.' for w in range(22)] for x in range(22)] for y in range(22)] for z in range(22)]
	data = ''

	with open(input_file, "r") as fp:
		data = fp.read().split('\n')

	for x in range(len(data)):
		
		for w in range(len(data[x])):

			pocket[11][11][7+x][7+w] = data[x][w]


	for i in range(6):
		print(f"Beginning iteration {i}")
		iterate(pocket)

	#print_pocket(pocket)
	
	count = 0

	for zz in pocket:
		for yy in zz:
			for xx in yy:
				for ww in xx:
					if ww == '#':
						count += 1

	print(f"The number of active cubes in the pocket dimension is {count}")



if __name__ == "__main__":
	input_file = f"input-d{day}.txt"

	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	main(input_file)
