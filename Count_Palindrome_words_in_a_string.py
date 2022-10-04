def palin(s):
    s = s.lower()
    return s==s[::-1]
s = input()
arr = s.split()
cnt=0
for i in arr:
    if palin(i):
        cnt+=1
print(cnt)
