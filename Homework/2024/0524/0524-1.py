s = "B023dky"
k = 3

res = ""

for ch in s:
    if "A" <= ch <= "Z":
        res += chr((ord(ch) - 65 + k) % 26 + 65)
    elif "a" <= ch <= "z":
        res += chr((ord(ch) - 97 + k) % 26 + 97)
    elif "0" <= ch <= "9":
        res += chr((ord(ch) - 48 + k) % 10 + 48)
    else:
        res += ch

print(res)