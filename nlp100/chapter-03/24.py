#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

m = re.compile(r"\[\[File\:(?P<p1>.+?)\|.+\]\]|\[\[ファイル\:(?P<p2>.+?)\|.+\]\]")
#得にコメントなし
#[File:*] or [ファイル:*]でマッチさせる。
#(?P<name>.+?)はテンプレ
with open("data02","rt") as f:
        for l in f:
                if m.match(l):
                        m_1 = m.search(l)
#m.serch(m,l)と同義
                        if m_1.group("p1"):
                                print(m_1.group("p1"))
                        if m_1.group("p2"):
                                print(m_1.group("p2"))
