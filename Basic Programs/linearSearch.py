n=(int)(input("Enter the size of the array"))
arr=[]
print("Enter the array elements")
for i in range(n):
  arr.append(input())
s=(int)(input("Enter the search element"))
c=0
for i in range(n):
  if s==arr[i]:
    c+=1
    print(s,"found at ",i+1,"position")
    break
if c==0:
  print("Element not found")
