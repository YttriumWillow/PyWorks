for i in range(0, 26):
    print('\t{', end = ' ')
    for j in range(0, 25):
        print( (i + j) % 26, end = ', ')
    print( (i + 25) % 26, '},')
