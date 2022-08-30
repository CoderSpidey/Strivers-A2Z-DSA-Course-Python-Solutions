toggle = 1
for i in range(5):
    for j in range(i+1):
        print((toggle+j)%2, end = ' ')
    print()
    toggle = 0 if toggle == 1 else 1