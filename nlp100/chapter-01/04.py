
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


s =""
s = s.replace(".","")
words = s.split(" ")
word_count = []
count = 0
for word in words:
	count+=1
	if count in [1,5,6,7,9,16,19]:
		word_count.append(word[:1])
	else:
		word_count.append(word[:2])

print(word_count)
#リスト内包表記を上手く使えばもっと上手く書けそう
