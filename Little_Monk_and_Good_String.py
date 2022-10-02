st = input()
cnt=0
mx=0
for i in st:
    d = ord(i)-97
    if d==0 or d==4 or d==8 or d==14 or d==20:
        cnt+=1
        if mx<cnt:
            mx = cnt
    else:
        cnt=0
print(mx)
