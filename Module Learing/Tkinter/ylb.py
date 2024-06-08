#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter as tk
import turtle as t
import sys
import time

top = tk.Tk()

L1 = tk.Label(top, text="输入：")
L1.pack()

E1 = tk.Entry(top, bd = 5, width = 100)
E1.pack()

L2 = tk.Label(top, text="广播内容：")
L2.pack()


E2 = tk.Entry(top, bd = 5, width = 100, xscrollcommand = 100)
E2.pack()

gbnr = ''
a = ''

def gb():
   a = E1.get()
   gbnr = '1234567890abcdefghijklmnopqrstuvwxyz(self translate system)' + E1.get() + '#!@$%%#@^%^*(OUT)'
   E2.delete(0, len(gbnr))
   E2.insert(0, gbnr)
   a = gbnr
   draw = []
   o = []
   for i in a:
      c = ord(i)
      d = hex(c)
      draw.append(c)
      o.append(d)
   t.setworldcoordinates(0, 0, 10000, 10000)
   t.speed(99999999999)
   t.hideturtle()
   t.goto(10000, 0)
   t.penup()
   t.goto(0, 7000)
   t.pendown()
   t.goto(0, 0)
   x = 0
   for i in draw:
      t.goto(x, int(i) * 50)
      x += 50
   t.goto(t.xcor() + 50, 0)
   for i in o:
      print(i)
   print('引力波发射完毕，威慑成功')
   top.destroy()
   time.sleep(5)
   sys.exit(0)

B1 = tk.Button(top, text ='点我，引力波宇宙广播将启动', command = gb, width = 100, bg = 'red', fg = 'white')
B1.pack()

top.mainloop()
