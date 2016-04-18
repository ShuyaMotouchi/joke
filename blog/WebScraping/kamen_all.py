#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup
import re


def read_kamen():
	url = "http://nendai-ryuukou.com/article/082.html"
	page = urllib.request.urlopen(url)
	s_p = page.read()
	s = BeautifulSoup(s_p)
	count=0
	for form in s.findAll("td"):
		for n in form:
			if len(n)>7:
				count +=1
				print(n)
	print("僕達は{0}人の仮面ライダー".format(count))



read_kamen()

