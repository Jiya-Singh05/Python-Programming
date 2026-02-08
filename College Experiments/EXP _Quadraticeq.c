#Check whether the quadratic equation has real roots or imaginary roots Display the roots
a=float(input("Enter the coefficient of x^2: "))
b=float(input("Enter the coefficient of x: "))
c=float(input("Enter the constant term: "))
if a==0:
    print("Invvalid quadratic")
else:
    d=b**2-4*a*c
    if d>0:
        r1=(-b + d**0.5)/ (2*a)
        r2=(-b - d**0.5)/ (2*a)
        print("roots are real and distinct") 
        print(f"Root are: {root1} {root2}")
    elif d==0:
        root=-b/(2*a)
        print("Roots are equal and real")
        print(f"Root: {root}")
    else:
        real=-b/(2*a)
        imag=-d**0.5/(2*a)
        print("Root are imaginary")
        print("Root1=",real,"+",imag,"i")
        print("Root2=",real,"-",imag,"i")
        
