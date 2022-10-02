st = input()
cnt=0
s=0
for i in st:
    if i=='R':
        s+=1
    else:
        s-=1
    if s==0:
        cnt+=1
print(cnt)