#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request


url = "http://www.pycon.jp/"

page = urllib.request.urlopen(url)
s = page.read()
print (s)
