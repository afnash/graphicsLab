li=[]
print("Enter 10 numbers")
for i in range(10):
 n=int(input())
 li.append(n)
largest = li[0]
for i in range(10):
 if li[i]>largest:
  largest = li[i]
print(f"largest number:{largest}")  
