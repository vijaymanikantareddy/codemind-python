t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    # print(arr)
    arr = sorted(arr)
    cnt = 0
    se = True
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if i==j:
                continue
            if arr[i]+arr[j] in arr:
                cnt += 1
                se = False
    if se:
        print(-1)
    else:
        print(cnt)