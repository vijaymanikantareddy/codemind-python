def ispalin(a):
    return a==a[::-1]

n = int(input())
for i in range(n):
    st = input()
    if ispalin(st):
        if len(st)%2==0:
            print('YES EVEN')
        else:
            print("YES ODD")
    else:
        print("NO")