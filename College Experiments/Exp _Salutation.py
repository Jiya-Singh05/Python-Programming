a=input("Enter name: ")
print("First letter:", a[0])
s=["Mr", "Mrs", "Ms", "Dr", "Prof", "mr","mrs","Engg","ms","dr"]
f=a.split()[0]
if f in s:
    print("It is a salutation")
else:
    print("It is not a salutation")
