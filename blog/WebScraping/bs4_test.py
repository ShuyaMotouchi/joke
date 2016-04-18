#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup


url = "http://www.pycon.jp/"


page = urllib.request.urlopen(url)
s_p = page.read()
s = BeautifulSoup(s_p)
a=[]
for form in s.findAll("span"):
	a = form
	print (a)
