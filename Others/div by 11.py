from math import *


number = int(input("三位数？: "))
g = number // 1 % 10
s = number // 10 % 10
b = number // 100 % 10
if abs( (g + b) - s ) % 11 == 0:
    print("Oh, my Lord, it could!")
else:
    print("Holy s**t, it couldn't!")


# 1254 21109