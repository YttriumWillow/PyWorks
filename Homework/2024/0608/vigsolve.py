vb = [[0] * 26 for _ in range(26)]

for i in range(26):
    for j in range(26):
        vb[i][j] = (i + j) % 26

# Here's to make trasfer table

phi = "aTT12AcKATdAwN!"
rho = "LEMON" # rho.upper()
sig = ""

i = 0; n = len(phi); k = len(rho)

# 倒序复用
# while len(rho) < n:
#     rho += rho[-2 : -k - 1 : -1]
    
while i < n:
    ch = phi[i]; key = ord(rho[i % k]) - 65 # 正序循环复用
    # key = ord(rho[i]) - 65 # 倒序复用
    if "a" <= ch <= "z":
        chx = ord(ch) - 97
        sig += chr(97 + vb[chx][key]) # or [key][chx] it's no big deal
    elif "A" <= ch <= "Z":
        chx = ord(ch) - 65
        sig += chr(65 + vb[chx][key])
    else:
        sig += ch
    i += 1

print (sig)

"""
aTT12|AcKAT|dAwN!
LEMON|LEMON|LEMO
lXF12|LgWOG|oEiB!

aTT12|AcKAT|dAwN!
LEMON|OMELE|MONO
lXF12|OoOLX|pOjB!

aTT12|AcKAT|dAwN!
IXF12|OpVEF|rNhR!
LEMON|ONLEM|ONLE
"""