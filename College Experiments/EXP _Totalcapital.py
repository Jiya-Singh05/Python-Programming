#count capital
text = input("Enter a string: ") 
count = 0
for ch in text:
    if ch.isupper(): 
        count=count+1 

print(f"Number of capital letters:{count}")
