n = int(input())
res=''
while n>0:
    d = n%26
    if d>0:
        res = chr(64+int(d))+res
        n=n//26
    else:
        res = 'Z'+res
        n = n//26 - 1
    
print(res)