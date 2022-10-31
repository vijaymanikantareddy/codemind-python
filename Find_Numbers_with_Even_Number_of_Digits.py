n = int(input())
cnt = 0
arr = list(map(int, input().split()))
for ele in arr:
    if len(str(ele))%2==0:
        cnt += 1
print(cnt)