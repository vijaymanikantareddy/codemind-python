n = int(input())
a = 0
b = 1
c = a + b
if n==1:
    print(a)
elif n==2:
    print(a,b)
else:
    print(a,b, end= ' ')
    for i in range(n-2):
        print(c, end=' ')
        a = b
        b = c
        c = a + b
        