#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
from io import StringIO

with open("jawiki-country.json",'rt') as open_file:
    for line in open_file:
        jdata = json.load(StringIO(line))
        if jdata["title"] == "イギリス":
            data = jdata["text"]

print(data)
