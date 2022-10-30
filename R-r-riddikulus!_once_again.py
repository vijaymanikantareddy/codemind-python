n, r = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(r, n):
    print(arr[i], end=' ')
for i in range(r):
    print(arr[i], end=' ')