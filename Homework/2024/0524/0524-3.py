s = "bh123hbn"; k = 3; n = len(s)
k %= len(s)
res = ""
for i in range(n):
    res += s[(i + k) % n]
print(res)