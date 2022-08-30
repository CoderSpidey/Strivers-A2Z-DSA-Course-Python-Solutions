x = '4' * 4
t = 4
for i in range(4):
    x = x[:i] + (str(t) * (4-i))
    print(x + x[::-1][1:])
    t -= 1
t = 2
for i in range(3):
    x = x[:len(x)-i-1] + (str(t) * (i+1))
    print(x + x[::-1][1:]) 
    t += 1

