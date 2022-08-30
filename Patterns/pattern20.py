for i in range(1,6):
    t = ('*' * i)+ (' ' * abs(5-i))
    print(t + t[::-1])
for i in range(1,5):
    t = ('*' * (5-i)) + (' ' * i)
    print(t + t[::-1])