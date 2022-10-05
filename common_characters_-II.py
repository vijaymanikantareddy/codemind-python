s1=input().lower()
s2 = input().lower()
a = set(s1)
b = set(s2)
cnt = 0
for i in a:
    if i in b and i!=' ':
        cnt+=1
print(cnt)