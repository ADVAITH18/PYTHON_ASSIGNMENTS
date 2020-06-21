"""
Program: Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.
Eg: format("05/08/2019")->2019/08/05

"""
def format(date):
    l=date.split('/')#splits the string based on given delimiter '/' and returns a list
    s=l[2]+'/'+l[1]+'/'+l[0]
    return s
d=input("Enter the date in DD/MM/YYYY format ")
print(format(d))
