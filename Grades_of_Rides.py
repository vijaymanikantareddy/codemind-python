a,b,c = map(int, input().split())
p=q=r=False
if a>50:
    p = True
if b>60:
    q = True
if c>100:
    r = True
if p and q and r:
    print(10)
elif p and q:
    print(9)
elif q and r:
    print(8)
elif p and r:
    print(7)
elif p or q or r:
    print(6)
else:
    print(5)