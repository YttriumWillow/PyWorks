from mtranslate import *
import time



f1 = open("tr.txt", "r", encoding = "utf-8")
f2 = open("pro.txt", "w+", encoding = "utf-8")

text1 = f1.read()
text2 = ""

for i in range(50):
    text2 = translate(text1, "en")
    text1 = translate(text2, "zh-CN")
    time.sleep(0.1)

print(text1)
f2.write(text1)

f1.close()
f2.close()