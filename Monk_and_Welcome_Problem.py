n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(len(a)):
    print(a[i]+b[i], end=' ')