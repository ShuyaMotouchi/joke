#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mechanicalsoup
import time
import os.path
import urllib

URL_login = ""
#URL_get = "http://30d.jp/img/gtb/6/12_large.jpg"
URL_get = ""

password = ""

#ブラウザ起動
br = mechanicalsoup.Browser()
#login pageの指定
login_page = br.get(URL_login)

#ログインフォームをしていする。
#br.select_form(nr=0)と同じような意味
login_form = login_page.soup.select("form")[0]

#値の入力
login_form.select("#password")[0]['value'] = password
#submit フォーム
br.submit(login_form,login_page.url)

time.sleep(5)
page = br.get(URL_get)
a_list = page.soup.find_all("a",class_="user_img user_img_detail photo")
for a in a_list:
  print(a.get("src"))
