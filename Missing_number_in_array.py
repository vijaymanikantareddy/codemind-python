t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    sa = n*(n+1)//2
    sb = sum(arr)
    print(sa-sb)