s = "hello world!"; k = 5
res = ""
for i in range(k):
    res += s[i::k]
print(res)