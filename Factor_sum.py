def factorsum(n):
	su = 0
	for i in range(1, n+1):
		if n%i==0:
			su += i
	return su

s = list(map(int, input().split(',')))
s.sort()
n = len(s)
flag = True
for ele in s:
	elesum = factorsum(ele)
	if elesum in s:
		c = 1
		print(ele, end=' ')
		flag = False
if flag:
	print("-1")