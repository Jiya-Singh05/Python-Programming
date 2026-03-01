n = int(input("Enter number of values: "))
data = [] #create list
for i in range(n):
    num = int(input("Enter value 0-3: "))
    if 0 <= num <= 3:
        data.append(num)   # add element in list
    else:
        print("Invalid input.")  #if no. is not between 0-3
        
data=tuple(data)  #list to tuple

count0 = data.count(0)  #counting occurence
count1 = data.count(1)
count2 = data.count(2)
count3 = data.count(3)

total = sum(data)   #calc sum
average = total / len(data)  #calc avg

print("\nTuple:", data)
print(f"0 occurred- {count0} times")
print(f"1 occurred- {count1} times")
print(f"2 occurred- {count2} times")
print(f"3 occurred- {count3} times")
print(f"Average:{average}")
