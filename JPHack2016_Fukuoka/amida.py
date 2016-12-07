#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask, render_template
import random

app = Flask(__name__)
rand_list = ["Bio-Z","if すゐか","multi-dimension","patchworks","Prepares","Skippo","ありおりはべり","せんしんぐー","ち～むどい☆けん","チームブライアンあと1単位"]
fi_str=[]

@app.route("/")
def hello():
    return render_template("index.html", title="ご注文はうさぎですか?")


@app.route("/ppap")
def ppap():
    return render_template("ppap.html",title="I have a")
   
@app.route("/timer")
def timer():
    return render_template("time.html",title="制限時間")

@app.route('/hello')
def index():
    random.shuffle(rand_list)
    fi_str=[]
    for (i,x) in enumerate(rand_list):
        f=str(i+1)+":"+x+"  "
        fi_str.append(f)
    fi_str = ' '.join(fi_str)
    return render_template("hello.html", title="ご注文はうさぎですか?",num = fi_str)

    
if __name__ == '__main__':
    app.debug = True
    app.run()
    #app.run(host='0.0.0.0')
