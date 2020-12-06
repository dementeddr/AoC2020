count = 0

with open("input-d6.py", "r") as fp:
	
	questions = {}

	for line in fp:
		
		if line == '\n':
			count += len(questions)
			print(f"{count}   {len(questions)}\n")
			questions = {}
			continue

		for q in line[:-1]:
			questions[q] = 1

		print(f"{line[:-1]}  {len(questions)}")

print(count)
