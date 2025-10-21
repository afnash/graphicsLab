li=[]
n=int(input("enter limit: "))
print(f"enter {n} numbers") 
for i in range(n):
	x=int(input())
	li.append(x)
largest=li[0]
for i in range(n-1):
	for j in range (1,n-i-1):
		if li[j]>li[j+1]:
			li[j],li[j+1]=li[j+1],li[j]
print(li)
