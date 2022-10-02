st = input()
cnt=1
for i in range(1, len(st)):
    if(ord(st[i])>=65 and ord(st[i])<=91):
        cnt+=1
print(cnt)