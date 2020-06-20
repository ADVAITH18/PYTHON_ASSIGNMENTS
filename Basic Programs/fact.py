"""
Program: To find the factorial of a number.
Eg: 5!=  5x4x3x2x1 =120

"""
n=(int)(input("Enter the number: "))
f=1
for i in range(1,n+1):
    f*=i
print("Factorial of ",n," is ",f)
