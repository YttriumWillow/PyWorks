from tkinter import *

def f():
    L.insert(0, 'Hello, world!')
    LC.insert(0, 'L insert a str \"Hello, world!\"')

def show():
    L.insert(0, '我被点了一下~')
    LC.insert(0, 'L insert a str \"我被点了一下~\"')

def del_():
    s = L.get(0)
    L.delete(0)
    LC.insert(0, 'L delete a str \"' + s + '\"')


top = Tk()

S1 = Scrollbar(top)
S2 = Scrollbar(top)

L = Listbox(top, yscrollcommand = S1.set)
LC = Listbox(top, width = 30, yscrollcommand = S2.set)

#side指定Listbox为居左
#下面的这句是关键：指定Scrollbar的command的回调函数是Listbar的yview
S1['command'] = L.yview
S2['command'] = LC.yview

TEXT = Text(top, width = 37, height = 2, undo = True, autoseparators = False)
TEXT.insert(INSERT, '插入组件')
TEXT['state'] = 'disabled'

BT = Button(top, text = '点我添加一行', command = show, padx = 10)
BD = Button(top, text = '点我删除一行', command = del_, padx = 10)

# 插入图片
# TEXT.insert(INSERT, '插入图片')

# photo = PhotoImage(file='G:\\无标题.png')
# TEXT.image_create(END, image=photo)

TEXT.pack()
L.pack(side = LEFT)
S1.pack(side = LEFT,fill = Y)
LC.pack(side = LEFT)
S2.pack(side = LEFT,fill = Y)
TEXT.window_create(INSERT, window = BT)
TEXT.window_create(INSERT, window = BD)
TEXT.insert(INSERT, '\n')
top.title("")
top.mainloop()