#!/usr/bin/python3

import re


fuzzy_shape = re.compile(r"#.+\s.*#.{4}##.{4}##.{4}###.*\s.*(?:#..){6}")

with open("test-input.txt", "r") as fp:

	pic = fp.read()

	print(fuzzy_shape.findall(pic))
