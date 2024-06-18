s = "hello world!"; key = [4, 1, 5, 3, 2]
k = len(key); n = len(s)
res = ""; l = 0

while l + k < n:
    t = ["*"] * len(key)
    for i in range(k):
        t[key[i] - 1] = s[l + i]
    res += "".join(t)
    l += k
res += s[l:]

print(res)