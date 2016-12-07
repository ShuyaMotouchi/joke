#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
m = re.compile(r'(==\w+==)|(===\w+===)|(====\w+====)')
#'|' 演算子は決して貪欲 (greedy) ではありません。
#分割しながら\Wで[a-zA-Z0-9_]とマッチする
with open("data02","rt") as f:
        for l in f:
                if m.match(l):
                        m_1 = m.search(l)
#m.serch(m,l)と同義
                        if m_1.group(1):
                                print(m_1.group(1)[2:-2],1)
#[2:-2]で"=="を削る
                        if m_1.group(2):
                                print(m_1.group(2)[3:-3],2)
                        if m_1.group(3):
                                print(m_1.group(3)[4:-4],3)


