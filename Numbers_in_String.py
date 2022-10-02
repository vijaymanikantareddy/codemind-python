st = input()
s=0
for i in st:
    d = ord(i)-48
    if d>=0 and d<=9:
        s+=d
print(s)