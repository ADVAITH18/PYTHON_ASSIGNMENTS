"""
Program: To find if a givn number is a special no: or not.
A special no: is one in which sum of factorials of its digit is eual to the number itself.

Eg: 145 = 1!+4!+5! = 1+24+120 = 145
"""
def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
n=(int)(input("Enter the number: "))
r,s=n,0
while r>0:
    s+=fact(r%10)
    r//=10
if s==n:
    print(n," is a special number")
else:
    print(n," is not a special number")
