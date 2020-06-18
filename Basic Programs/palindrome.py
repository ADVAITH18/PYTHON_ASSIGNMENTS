n=int(input("Enter the number "))
i,r=n,0
while(i>0):
    r=r*10+i%10
    i=i//10
if n==r:
    print(n," is a palindrome number")
else:
    print(n," is not a palindrome number")
