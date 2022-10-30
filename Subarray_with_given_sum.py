t = int(input())
for _ in range(t):
    n, re = map(int,input().split())
    arr = list(map(int, input().split()))
    ans = []
    se = True
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if sum(arr[i:j+1])==re:
                ans.append(i+1)
                ans.append(j+1)
                se = False
    if se:
        print(-1)
    else:
        print(ans[0], ans[1])