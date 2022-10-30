n = int(input())
arr = list(map(int, input().split()))
res = []
for i in range(len(arr)):
    se = True
    for j in range(i+1, len(arr)):
        if arr[j]>arr[i]:
            res.append(j-i)
            se = False
            break
    if se:
        res.append(0)
for ele in res:
    print(ele, end=' ')