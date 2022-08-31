a = input()
res=0
for i in range(len(a)):
    res += int(a[i])**(i+1)
print(str(res)==a)