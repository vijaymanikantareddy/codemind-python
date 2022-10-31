n = int(input())
arr = list(map(int, input().split()))
for i in range(len(arr)):
    cnt = 0
    for j in range(len(arr)):
        if i==j:
            continue
        if arr[i]>arr[j]:
            cnt += 1
    print(cnt, end = ' ')