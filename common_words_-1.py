ar = input().upper().split()
br = input().upper().split()
cnt=0
for ite in ar:
    for val in br:
        if ite==val:
            cnt+=1
print(cnt)