n, t = map(int, input().split())
li = list(map(int, input().split()))
cnt = 0
for i in range(0, n):
    for j in range(i, n):
        if sum(li[i:j+1]) == t:
            cnt+=1
print(cnt)