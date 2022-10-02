st = input()
h=0
v=0
for i in st:
    if i=='U':
        v+=1
    elif i=='D':
        v-=1
    elif i=='R':
        h+=1
    else:
        h-=1
print(h==0 and v==0)
    