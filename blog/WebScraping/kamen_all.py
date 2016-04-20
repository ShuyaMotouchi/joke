#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup


url = "http://nendai-ryuukou.com/article/082.html"
page = urllib.request.urlopen(url)
s_p = page.read()
s = BeautifulSoup(s_p)
count=0
for form in s.findAll("td"):
	for n in form:
		if len(n)>7:
			if n[:2]=="仮面":	
				count +=1
				print("{0}:{1}".format(count,n))
				
print("僕達は{0}人の仮面ライダー".format(count))


