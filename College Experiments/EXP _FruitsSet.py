#Create 2 sets s1 and s2 of n fruits each by taking input from user and find:1).Fruits which are in both sets s1 and s2 2).Fruits only in s1 but not in s23).Count of all fruits from s1 and s2.
total=int(input("Enter number of fruits you want to add: "))

print("Enter fruits in set 1: ")
s1=set()
for i in range(total):
    fruit = input()
    s1.add(fruit) 
    
print("Enter fruits in set 2: ")    
s2=set()
for i in range(total):
    fruit = input()
    s2.add(fruit)  

print(f"Fruits in both sets: {s1 & s2}")   
print(f"Fruits in set 1: {s1}")
print(f"Fruits in set 2: {s2}")
print(f"Fruits only in s1 but not in s2: {s1 - s2}") 
print(f"Fruits only in s2 but not in s1: {s2 - s1}") 
print(f"Total fruits: {len (s1 | s2)}")

