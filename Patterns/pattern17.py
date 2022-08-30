t = 'A'
for i in range(4):
    x = ' ' * (4-len(t)) + t + t[::-1][1:]
    print(x)
    t = t + chr(ord(t[-1]) + 1)
