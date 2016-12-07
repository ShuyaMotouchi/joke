#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re


match = re.compile(r'\[\[Category\:(((?P<m2>.*?)\|+.*)|(?P<m1>.*?))\]\]')

with open("data02","rt") as f:
	for l in f:
		if match.match(l):
			match01 = match.search(l)
			if match01.group("m2"):
                		print(match01.group("m2"))
			elif match01.group("m1"):
				print(match01.group("m1"))
