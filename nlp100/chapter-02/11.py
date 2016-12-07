#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#trコマンド
"""
	python3 12.py 置換前 置換後

"""


import sys


def tra(file1,val1,val2):
	try:
		with open(file1) as f:
			f = f.read()
	except:
		print("miss")
	finally:
		print(f.replace(val1,val2))

if __name__=='__main__':

	print (tra(sys.argv[1],sys.argv[2],sys.argv[3]))
