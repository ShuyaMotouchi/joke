# -*- coding: utf-8 -*-
#%!/bin/bash python3

import random
from matplotlib import pyplot as plt

def zundoko():
	while True:
		rand = random.randint(1,2)
		if rand == 1:
			print("====ズン====")
			return(1)
		elif rand == 2:
			print("====ドコ====")
			return(2)


def kiyoshi(): 
	l=[]
	p=[]
	while True:
		l.append(zundoko())
		zun = l.count(1)
		doko = l.count(2)
		p = l[-5:]
		if p == [1,1,1,1,2]:
			print ("=き・よ・し=")
			break
	fig = plt.figure(figsize=(4, 4))
	ax = fig.add_subplot(111)
	ax.pie([zun,doko])
	plt.show()
	print ("ズンの回数 青:%d" %zun)
	print ("ドコの回数 緑:%d" %doko)


kiyoshi()
