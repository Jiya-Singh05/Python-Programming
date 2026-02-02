#Check whether the quadratic equation has real roots or imaginary roots.Display the roots

a=float(input("Enter the coefficient of x^2:"))
b=float(input("Enter the coefficient of x:"))
c=float(input("Enter the constant term:"))

root=((b**2) - 4*a*c)
r1=((-b)+root**0.5)/(2*a)
r2=((-b)-root**0.5)/(2*a)

if(root>0):
    print(f"roots are real and distinct, roots:{r1},{r2}")
elif(root==0):
    print(f"roots are real and equal, roots:{r1},{r2}")
else:
    print("roots are imaginary")
