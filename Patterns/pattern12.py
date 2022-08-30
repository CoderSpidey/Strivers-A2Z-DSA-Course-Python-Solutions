for i in range(1,5):
    t = ''
    for j in range(1,i+1):
        t += str(j)
    t += ' ' * (4-(len(t)))
    print(t + t[::-1])

        