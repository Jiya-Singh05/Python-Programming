#Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number. 
def sumcubes(n):   #defining function
    total=0
    for i in range(1, n):
        total=total + i**3    #adding cubes
    return total

n=int(input("Enter a positive integer: "))
result=sumcubes(n)                    #calling function
print(f"Sum of cubes of positive integers smaller than {n} is: {result}")
