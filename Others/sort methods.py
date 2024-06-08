l = [5, 4, 3, 2, 1]
t = [4, 1, 7, 5, 3]
for i in range(len(t) - 1):
    for j in range(len(t) - i - 1):
        if t[j] > t[j + 1]:
            t[j], t[j + 1] = t[j + 1], t[j]
print(t)

def mppx(t):
    for i in range(len(t) - 1):
        for j in range(len(t) - i - 1):
            if t[j + 1] < t[j]:
                t[j], t[j + 1] = t[j + 1], t[j]
    return t

def xzpx1(t):
    for i in range(len(t) - 1):
        minp = i
        for j in range(i, len(t)):
            if t[j] < t[minp]:
                minp = j
        t[i], t[minp] = t[minp], t[i]
    return t

def crpx(t):
    for i in range(1, len(t)):
        x = t[i]
        j = i - 1
        while j >= 0 and t[j] < x:
            t[j + 1], t[j] = t[j], t[j + 1]
            j -= 1
        t[j + 1] = x
    return t

def xzpx2(t):
    for i in range(len(t) - 1):
        minp = i
        for j in range(i, len(t)):
            if t[j] < t[minp]:
                t[j], t[minp] = t[minp], t[j]
    return t

def kspx1(t):
    if len(t) < 2:
        return t
    else:
        m = t[0]
        l = [i for i in t if i < m]
        r = [i for i in t if i >= m]
        return kspx1(l) + [m] + kspx1(r)

def kspx2(t):
    if len(t) >= 2:
        m = t[len(t) // 2]
        l, r = [], []
        t.remove(m)
        for n in t:
            if n >= m:
                r.append(n)
            else:
                l.append(n)
        return kspx2(l) + [m] + kspx2(r)
    else:
        return t



print(mppx(l))
print(xzpx1(l))
print(xzpx2(l))
print(crpx(l))
print(kspx1(l))
print(kspx2(l))
print(l)
