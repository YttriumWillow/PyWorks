from os import *
import base64

req = input("tmd 给我把你那个傻逼问题写在这: ")

p = base64.b64encode(req.encode('utf-8'))
fuck = str(p, 'utf-8')

system("cmd /c start  https://btfy.ur1.fun/?q=" + fuck)
system("cmd /c start  https://lmstfy.net/?q=" + fuck)
system("cmd /c start  https://lmstfy.net/bing/?q=" + fuck)