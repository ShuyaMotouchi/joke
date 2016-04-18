#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import mechanize

url = "http://kyusyu.machi.to/kyusyu/#1"

br = mechanize.Browser()
page = br.open(url)

br.select_form(nr=0)
br["NAME"]="Fred"
br["MESSAGE"]="hello world"
br.submit()
