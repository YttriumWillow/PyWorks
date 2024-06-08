import requests
import time
url = 'http://translate.google.cn/translate_a/single?'
def ft(text):
    flag1 = 0
    flag2 = True
    ansl = []
    for i in text:
        if flag1 >= 2:
            break
        elif i == '"':
            flag1 += 1
            flag2 = True - flag2
        elif flag2 == False:
            ansl.append(i)
    w = ''.join(ansl)
    return w
    # return ansl
def etoc(t):
    x = requests.get('http://translate.google.cn/translate_a/single?client=at&sl=en&tl=zh-CN&dt=t&q=' + t)
    return ft(x.text)
def ctoe(t):
    x = requests.get('http://translate.google.cn/translate_a/single?client=at&sl=zh-CN&tl=en&dt=t&q=' + t)
    return ft(x.text)

# [[["你好","hello",null,null,10]],null,"en",null,null,null,null,[]]

f1 = open("tr.txt", "r", encoding = "utf-8")
f2 = open("pro.txt", "w+", encoding = "utf-8")

i1 = f1.read()
print(i1)
i2 = ''

for i in range(0, 10):
    i2 = ctoe(i1)
    print(i2)
    i1 = etoc(i2)
    print(i1)
    time.sleep(0.1)

f2.write(i1)

f1.close()
f2.close()