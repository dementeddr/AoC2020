count = 0

with open("input-d6.py", "r") as fp:
	
	questions = {}
	people = 0

	for line in fp:
		
		if line == '\n':
			
			for q in questions:
				if questions[q] == people:
					count += 1

			print(questions)
			print(people)
			print(count)
			print()

			questions = {}
			people = 0
			continue

		for q in line[:-1]:
			questions[q] = questions.get(q, 0) + 1
		
		people += 1


		print(line)

print(count)
