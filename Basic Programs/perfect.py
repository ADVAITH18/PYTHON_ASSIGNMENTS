"""
Program: To check whether a number is perfect or not.A number is said to be perfect
if the sum of all factors except the number itself is equal to the number.

Eg: 6
1+2+3=6
"""
n=(int)(input("Enter the number "))
s=0
for i in range(1,n//2+1):
    if n%i==0:
        s+=i
if s==n:
    print(n," is a perfect number")
else:
    print(n," is not a perfect number")
