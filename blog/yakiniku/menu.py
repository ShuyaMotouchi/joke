#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np,pandas as pd
from wordcloud import WordCloud



def new_menu():
    menu = ["本陣カルビ","中落ちカルビ","サガリ","厚切りカルビステーキ","塩豚カルビ","塩鶏モモ","塩センマイ" ,"塩レバー","塩トントロ","塩豚タン",\
"塩ヤゲンナンコツ","塩しま腸","塩サイコロトンテキ","味噌豚カルビ","味噌鶏モモ","味噌センマイ","味噌レバー","味噌ヤゲンナンコツ", \
    "味噌しま腸","ピリ辛豚カルビ","ピリ辛鶏モモ","ピリ辛センマイ","ピリ辛レバー","ピリ辛ヤゲンナンコツ","ピリ辛しま腸","ネギ塩豚タン",\
    "ウインナー","にんにく焼き","キャベツ","ピーマン","たまねぎ","トウモロコシ","カボチャ","エリンギ","焼野菜盛り合わせ","サンチュ","本陣サラダ","チョレギサラダ",\
    "ツナタマサラダ","ナムル","キムチ","カクテキ","キムチ2種盛","もやしナムル","ワカメスープ","たまごスープ","牛すじ煮込み","韓国のり","ごはん（小）","ごはん（中）",\
    "ごはん（大）","ビビンバ","りんごシャーベット","きなこバニラ","バニラアイス","チョコバニラ","フルーツポンチ","ストロベリーアイス",
    ]

    price = [518,734,734,834,410,410,518,518,518,518,\
        572,572,518,464,464,572,572,564,\
        572,464,464,572,572,464,572,572,\
        410,302,248,248,248,248,248,248,464,302,518,518,\
        580,302,302,302,410,302,410,410,410,194,216,216,\
        216,734,248,248,248,248,248,248,
        ]
        
    many_menu = []    
    for n in range(len(menu)):
        for a in range(price[n]):
            many_menu.append(menu[n])
    return many_menu

def create_wordcloud(text):
    fpath = "/usr/share/fonts/truetype/takao-mincho/TakaoExMincho.ttf"
    wordcloud = WordCloud(background_color="black",font_path= fpath ,width=900, height=500).generate(text)

    plt.figure(figsize=(15,12))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig("graph.png")
    plt.show()

if __name__ == '__main__':
    menu_list = new_menu()
    print(" ".join(menu_list))
    create_wordcloud(" ".join(menu_list))
