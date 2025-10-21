li=[]
print("enter 10 numbers: ")
for i in range(10):
	x=int(input())
	li.append(x)
largest=li[0]
for i in range(1,10):
	if li[i]>largest:
		largest = li[i]
print(f"largest of these 10 is: {largest} ") 
