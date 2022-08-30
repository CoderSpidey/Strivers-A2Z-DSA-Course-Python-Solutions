t = 'E'
for i in range(5):
    for j in range(i+1):
        print(chr(ord(t) + j), end = ' ')
    print()
    t = chr(ord(t) - 1)