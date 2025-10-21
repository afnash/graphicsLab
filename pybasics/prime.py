x=int(input("enter any number:"))
count=0
for i in range(1,int(x/2)+1):
	if (x % i == 0):
		count+=1
if count>1:
	print(f"{x} is not prime.")
else:
	print(f"{x} is  prime.")
