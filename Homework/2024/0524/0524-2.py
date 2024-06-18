s = "bh123hbn"; k = 3

k %= len(s)

res = s[k:] + s[:k]

print(res)