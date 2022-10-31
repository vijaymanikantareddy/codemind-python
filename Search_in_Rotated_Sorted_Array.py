n = int(input())
arr = list(map(int, input().split()))
e = int(input())
se = True
for i in range(len(arr)):
    if e == arr[i]:
        print(i)
        se = False
        break
if se:
    print(-1)