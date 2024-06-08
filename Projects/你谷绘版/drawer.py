# -*- coding: utf-8 -*-

# FileName: draw.py
#     + randomhash: f40596
# Author: fengziyi
#     + base64: ZmVuZ3ppeWk=
#     + MD5: 9b0454ce8364ba54b28c8b9b7f9dafc7
# Date: 2022/12/17 星期六
# Time: 18:14:21
#     + Unix Timestamp(second): 1671272061
# Encoding: UTF-8
#     + Encodeing Test: 哦，你使用了UTF-8编码。不是么？ovo
# Copyright: fengziyi
# 唯一所有权利者: fengziyi

from PIL import Image
from time import *
# from requests import *
import requests
import io


# 提交请求的网址(最后带一个问号)
url = "https://segonoj.site/paintboard/paint?"
# 网站限定的提交间隔时间(单位：秒)
waitTime = 5
# 网站给的 token
token = "txmt8TDnzReNKMChbijQ8033jYxHDd0yQMahWpH4TtHGYhemJT"
# 起始作画位置(x, y)
startPixel = (800, 75)
# 图像位置(在线)
imageLocation = R"D:\LEGION\Desktop\CrOthers\Objects\head_awa\nahidax.jpg"
imageLocation = R"https://ldbbs.ldmnq.com/bbs/topic/attachment/2022-12/c08d1344-010b-4a48-9ac3-f0002c642d9a.jpg"



# request initalize 
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
# picture initalize
response = requests.get(imageLocation, headers = header)
img = Image.open(io.BytesIO(response.content))
print("已获取图片:", img)
width, height = img.size

# main thread
print("信息获取完毕!")
print("图像信息:")
print("width: %d   height: %d" % (width, height))
print("request location:", imageLocation)

def getcolor(x): # RGB to hex
    return ("#" + \
    hex(x[0]).lstrip("0x").rstrip("L") + \
    hex(x[1]).lstrip("0x").rstrip("L") + \
    hex(x[2]).lstrip("0x").rstrip("L"))

for i in range(0, height):
    print("Now:", "%.2f" % (i / height * 100), "%")
    for j in range(0, width):

        # get pixel
        pixel = img.getpixel( (j, i) )
        x = startPixel[0] + j
        y = startPixel[1] + i
        color = getcolor(pixel)

        # how to debug : work here
        # sample : x=114&y=514&color=0&uid=114514&token=114514
        now = "x=%d&y=%d&color=%s&uid=&token=%s" % (x, y, color, token)


        # send requests
        requests.get(url + now, headers = header)
        print("Now:", "%.2f" % ((i * width + j) / (width * height) * 100), "%")
        print(url + now)
        sleep(waitTime)
input()