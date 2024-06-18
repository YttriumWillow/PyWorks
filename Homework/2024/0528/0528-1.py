s = "h dew!lolrol"; k = 5
n = len(s); cur = 0
res = ["*"] * n
for i in range(k):
    p = i
    while p < n:
        res[p] = s[cur]
        p += k; cur += 1
print("".join(res))