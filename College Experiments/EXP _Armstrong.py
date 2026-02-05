#Check whether the given number is an armstrong number or not
n=int(input("Enter number: "))
a=n
b=n
total=0
ans=0
while(n!=0):
   n= n//10
   total=total+1
while(a!=0):
    rem=a%10
    ans=ans+(rem)**total
    a=a//10
if(ans==b):
    print("It is an armstrong number")
else:
    print("Not an armstrong number")
