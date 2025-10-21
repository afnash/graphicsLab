li=[]
n=int(input("Enter the length of list"))
print("Enter the numbers:")
for i in range(n):
 num=int(input())
 li.append(num)
for i in range(n-1):
 for j in range(n-i-1):
  if li[j]>li[j+1]:
   li[j],li[j+1] = li[j+1],li[j] 
print("Sorted list:",li)   
