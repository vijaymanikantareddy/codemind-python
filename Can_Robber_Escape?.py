n = int(input())
a = list(map(int, input().split()))[:n]
cnt=0
for i in a:
    if i%2!=0:
        cnt+=1
if cnt<=2:
    print("YES")
else:
    print("NO")