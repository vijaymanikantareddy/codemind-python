a = int(input())
b = int(input())
li = [i for i in range(a, b+1)]
cnt = 0
for i in range(0, len(li)):
    for j in range(i, len(li)):
        if sum(li[i:j+1])%2 != 0:
            cnt+=1
print(cnt)