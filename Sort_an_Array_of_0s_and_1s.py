n = int(input())
li = list(map(int, input().split()))[:n]
zc = 0
for i in li:
    if i==0:
        zc+=1
for i in range(zc):
    print(0, end=' ')
for i in range(zc, len(li)):
    print(1, end=" ")