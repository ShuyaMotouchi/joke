
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def ngram(input,n):
	l = len(input) - n+1
	r = []
	for i in range(0,l):
		r.append(input[i:i+1])
	return r

ngram()
#非完成
