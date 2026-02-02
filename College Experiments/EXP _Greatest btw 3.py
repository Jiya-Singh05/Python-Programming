#Find the greatest among three numbers assuming no two values are same
a=float(input("Enter your no.a:"))
b=float(input("Enter your no.b:"))
c=float(input("Enter your no.c:"))

if(a>b and a>c):
    print("a is greater")
elif(b>c and b>c):
    print("b is greater")
else:
    print("c is greater")
