#Check whether given number is palindrome or not. 
n=int(input("Enter a number: "))
a=n
rev=0
while(n!=0):
    rem=n%10
    rev=rem+rev*10
    n=n//10
if(a==rev):
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")
