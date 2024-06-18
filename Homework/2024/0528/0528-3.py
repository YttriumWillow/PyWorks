s = "eolhlwlr od!"; key = [4, 1, 5, 3, 2]
k = len(key); n = len(s)
res = ""; l = 0

while l + k < n:
    t = ["*"] * len(key)
    for i in range(k):
        t[i] = s[l + key[i] - 1]
    res += "".join(t)
    l += k
res += s[l:]

print(res)