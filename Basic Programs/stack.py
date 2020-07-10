"""
Program: Implement stack using Python, it can be implemented using lists in python.
  Instead of push() we can use append()
  We can also use pop() function along with lists

Author:Advaith 
"""
stack=[]
size=(int)(input("Enter the size of the stack "))

def push():
	if size==len(stack):
		print("STACK OVERFLOW")
	else:
		n=(int)(input("Enter the element "))
		stack.append(n)

def pop():
	if len(stack)==0:
		print("STACK UNDERFLOW")
	else:
		print("Popped item is ",stack.pop())


def display():
	print("The current stack is:")
	for i in range(len(stack)-1,-1,-1):
		print(stack[i])

while 1:
	print("Menu")
	print("1.Push")
	print("2.Pop")
	print("3.Display")
	print("4.Exit")
	ch=(int)(input("Enter your choice "))
	if ch==1:
		push()
	elif ch==2:
		pop()
	elif ch==3:
		display()
	elif ch==4:
		exit(0)
	else:
		print("Wrong Choice ")
