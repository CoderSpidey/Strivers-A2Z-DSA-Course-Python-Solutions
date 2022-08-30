for i in range(5):
    t = 'A'
    for j in range(5-i):
        print(t, end = '')
        t = chr(ord(t) + 1)
    print()