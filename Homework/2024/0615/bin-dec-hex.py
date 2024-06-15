optional = [None] * 7
hexV = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 0xA, "B": 0xB, "C": 0xC, "D": 0xD, "E": 0xE, "F": 0xF, }
hexC = "0123456789ABCDEF"
binV = {"0000": "0", "0001": "1", "0010": "2", "0011": "3", "0100": "4", "0101": "5", "0110": "6", "0111": "7", "1000": "8", "1001": "9", "1010": "A", "1011": "B", "1100": "C", "1101": "D", "1110": "E", "1111": "F"}
binC = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111", "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111"}

def _dec(d, k):
    if d == 0: return "0"
    res = ""
    while d > 0: res = hexC[d % k] + res; d //= k
    return res

# bin -> dec
optional[1] = lambda b: sum(int(v) * 2 ** k for k, v in enumerate(reversed(b)))
# dec -> bin-
optional[2] = lambda d: _dec(int(d), 2)
# hex -> dec
optional[3] = lambda h: sum(hexV[v] * 16 ** k for k, v in enumerate(reversed(h)))
# dec -> hex
optional[4] = lambda d: _dec(int(d), 16)
# bin -> hex
# lambda b: _dec(optional[1](b), 16)
optional[5] = lambda b: ''.join(
    binV[ b.zfill((len(b) + 3) // 4 * 4)[i : i + 4] ]
    for i in range(0, len(b), 4)
)
# hex -> bin
# lambda h: _dec(optional[3](h), 2)
optional[6] = lambda h: ''.join(
    binC[ char.upper() ] for char in h
).lstrip('0') or '0'

while True:
    opr = int(input("Option #"))
    inf = input("inf: ")
    ouf = optional[opr](inf)
    print("ouf:", ouf)
    
