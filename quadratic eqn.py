a=float(input("enter the number:"))
b=float(input("enter the number:"))
c=float(input("enter the number:"))
D=b*b-4*a*c
if D>0:
    print("Two real solutions")
elif D==0:
    print("One real solution")
else:
    print("No real solution")
