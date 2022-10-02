st = input()
mx = st[0]
for i in range(1, len(st)):
    if ord(st[i])>ord(mx):
        mx = st[i]
print(mx)