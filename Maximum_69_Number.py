def fun(n):
    n = str(n)
    l = [ch for ch in n]
    for i in range(len(l)):
        if l[i]=='6':
            l[i]='9'
            break
    s = 0
    for i in l:
        s = s*10 + int(i)
    return s

n = int(input())
print(fun(n))