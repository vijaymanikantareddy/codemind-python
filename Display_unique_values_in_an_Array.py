n = int(input())
arr = list(map(int, input().split()))[:n]
cnt = 0
res = []
for i in range(len(arr)):
    if arr[i]==-1:
        continue
    se = True
    for j in range(i+1, len(arr)):
        if(arr[i]==arr[j]):
            arr[j]=-1
            se = False
    if se:
        res.append(arr[i])
if len(res)==0:
    print(-1)
else:
    for i in res:
        print(i, end=' ')