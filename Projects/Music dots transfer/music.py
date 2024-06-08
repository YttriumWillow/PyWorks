# /playsound lkrb.piano.p62ff block @p ~ ~ ~ 2 1
from dots import *
import clipboard

ms = open("MusicDots.txt", "r", encoding = "utf-8")
line = ms.readline()

while line:
    tmp = line.split()
    print(tmp)
    putstr = "/playsound lkrb.piano.p" + dot[tmp[0]] + tmp[1] + " block @p ~ ~ ~ 2 1"
    print(putstr)
    clipboard.copy(putstr)
    input("Next...")
    line = ms.readline()
