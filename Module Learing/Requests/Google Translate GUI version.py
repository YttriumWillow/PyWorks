from tkinter import *
import requests

c = "en"
t = "zh-CN"
languages = {
    "英语" : "",
    "简体中文" : ""
    }
# url = 'http://translate.google.cn/translate_a/single?'
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
    x = requests.get('http://translate.google.cn/translate_a/single?client=gtx&sl=en&tl=zh-CN&dt=t&q=' + t)
    return ft(x.text)
def ctoe(t):
    x = requests.get('http://translate.google.cn/translate_a/single?client=gtx&sl=zh-CN&tl=en&dt=t&q=' + t)
    return ft(x.text)
def fanyi():
    T2.delete(1.0, END)
    x = requests.get('http://translate.google.cn/translate_a/single?client=gtx&sl=' + c + '&tl=' + t + '&dt=t&q=' + T1.get('1.0', END))
    T2.insert(END, ft(x.text))

top = Tk()

# S1 = Scrollbar(top)

T1 = Text(top, width = 50, height = 8, undo = True, autoseparators = False)# , yscrollcommand = S1.set
T2 = Text(top, width = 50, height = 8, undo = True, autoseparators = False)

# S1['command'] = T.yview

B1 = Button(top, width = 50, text = "翻译", command = fanyi)

T1.pack()
T2.pack()
B1.pack()

# 顶部菜单
menubar = Menu(top)

menubar.add_command(label = '源语言')#  , command = f1)
menubar.add_command(label = '目标语言')#  , command = f2)
top.config(menu = menubar)

# S1.pack(side = RIGHT,fill = Y)
top.title("Google Translate")
top.mainloop()