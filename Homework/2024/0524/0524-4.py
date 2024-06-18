s = "ABC12DZXasdf";  res = ""
f = False; l = 0; r = 0

for i in range(len(s)):
    ch = s[i]
    
    if "a" <= ch <= "z":
        if f: continue
        else: l = i; f = True
    elif f:
        print(( " ".join(s[l:i].upper()) )[::-1], end = " ")
        f = False
    
    if "A" <= ch <= "Z":
        print(ord(ch) - 65 + 1, end = " ")
    elif "0" <= ch <= "9":
        print(chr(ord(ch) - 48 + 65), end = " ")
        
if f: print(( " ".join(s[l:].upper()) )[::-1], end = " ")

print(res)