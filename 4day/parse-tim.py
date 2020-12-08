#!/usr/bin/python3

import re

pat = re.compile(r"'pid': '(\d{9})'")

with open("tim-output.txt", "r") as fp:

	for line in fp:
		print(pat.search(line).group(1))
