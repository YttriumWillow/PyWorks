s = "abcdefghijk"; res = 0
for i in range(1, len(s), 2):
    res += ord(s[i]) - ord(s[i - 1])
print (res)