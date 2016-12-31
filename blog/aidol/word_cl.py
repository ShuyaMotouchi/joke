#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import MeCab as mc
from bs4 import BeautifulSoup
import sys
from urllib import request
import time
import re 



def mecab_analysis(text):
    t = mc.Tagger("-Ochasen")
    t.parse('')
    node = t.parseToNode(text) 
    output = []
    while node:
        if node.surface != "":  # ヘッダとフッタを除外
            word_type = node.feature.split(",")[0]
            if word_type in ["形容詞", "動詞","名詞", "副詞"]:
                output.append(node.surface)
        node = node.next
        if node is None:
            break
    return output

def get_wordlist_from_blog(url):
    headers = {
                    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
                                          }
    req = request.Request(url, None, headers)
    res = request.urlopen(req)
    soup = BeautifulSoup(res.read(),'html.parser')
    #soup = soup.find(class_="box-article")
    text = soup.get_text()
    return mecab_analysis(text)
    #return text


def create_wordcloud(text):
    fpath = "/usr/share/fonts/truetype/takao-mincho/TakaoExMincho.ttf"

    stop_words = [ 'てる', 'いる', 'なる', 'れる', 'する', 'ある', 'こと', 'これ', 'さん', 'して', \
                   'くれる', 'やる', 'くださる', 'そう', 'せる', 'した',  '思う',  \
                   'それ', 'ここ', 'ちゃん', 'くん', '', 'て','に','を','は','の', 'が', 'と', 'た', 'し', 'で', \
                   'ない', 'も', 'な', 'い', 'か', 'ので', 'よう', '', 'れ','さ','なっ',\
                   'update','member','更新']

    wordcloud = WordCloud(background_color="black",font_path= fpath ,width=900, height=500, \
                            stopwords=set(stop_words)).generate(text)


    plt.figure(figsize=(15,12))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig("graph.png")
    plt.show()

#imoはページ数 ctはメンバー数
def page_info(url):
    url = url + "&ima=" + str(input("ページ数:")).zfill(4)
    url = url + "&cd=member&ct=" + str(input("メンバーの有効数:"))
    return url

url = "http://www.keyakizaka46.com/mob/news/diarKiji.php?site=k46o"
url = page_info(url)
wordlist = get_wordlist_from_blog(url)
print(wordlist)
print(" ".join(wordlist))
#create_wordcloud(" ".join(wordlist))
