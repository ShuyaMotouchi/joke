#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


with open("data02","rt") as f:
    for l in f:
        if re.match(r"\[\[Category\:.*\]\]",l):
          #.*で任意の０文字以上の文字列にマッチします
            print(l.strip())
