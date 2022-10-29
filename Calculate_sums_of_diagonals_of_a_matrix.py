n = int(input())
arr = []
for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)
l = 0
r = 0
for i in range(n):
    for j in range(n):
        if i==j:
            l += arr[i][j]
        if i+j==n-1:
            r += arr[i][j]
print("Principal Diagonal:{}".format(l))
print("Secondary Diagonal:{}".format(r))
