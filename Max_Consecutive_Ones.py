n = int(input())
arr = list(map(int, input().split()))
mx = arr[0]
s = 0
for i in range(len(arr)):
    if arr[i]==0:
        if mx < s:
            mx = s
        s = 0
    else:
        s += 1
if mx < s:
    mx = s
print(mx)
# print(arr)