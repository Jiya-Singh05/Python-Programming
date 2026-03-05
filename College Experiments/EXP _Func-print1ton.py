#Write a Python function to print 1 to n using recursion. (Note: Do not use loop) 
def printno(n):
    if n==0:      #if n becomes 0 then it stops
        return
    printno(n-1)   # calling functon again
    print(n)             # printing after recursion

n=int(input("Enter a number: "))
printno(n)
