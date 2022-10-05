dic = {0:'000', 1:'001',2:'010', 3:'011', 4:'100',5:'101',6:'110',7:'111'}
n = input()
res =''
for i in n:
    res += dic[int(i)]
i = 0
while(i<len(res)):
    if(res[i]=='1'):
        break
    i+=1
res = res[i:]
print(res)