
x = ["C", "xC", "D", "xD", "E", "F", "xF", "G", "xG", "A", "xA", "B"]
y = [2, 3, 4, 5, 6, 7, 8]

start = 24

for i in y:
    for j in x:
        print("\"", j, i, "\"",  " : ", "\"", start, "\"", ",", sep = "")
        start += 1