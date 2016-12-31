#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import sys
from urllib import request
import os.path
import os
import time
import re 
import cv2

# 認識対象ファイルの指定
image_path = "sub-member-6451_jpg.jpg"
# 認識対象ファイルの読み込み
image = cv2.imread(image_path)

#ORV(Oriented FAST and Rotated BRIEF)
detector = cv2.ORB_create()

# 特徴検出
keypoints = detector.detect(img)

# 画像への特徴点の書き込み
out = cv2.drawKeypoints(img, keypoints, None)

# 表示
cv2.imshow("keypoints", out)
