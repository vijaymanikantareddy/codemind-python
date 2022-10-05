n = int(input())
for i in range(n):
    for j in range(1,n-1):
        print(j,end='')
    for k in range(n-3,0,-1):
        print(k,end='')
    print()