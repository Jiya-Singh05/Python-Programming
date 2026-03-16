n=int(input("Enter number of students: "))
stu={}  #create dict

for i in range(n):
    name=input("Enter name: ")  #take input name
    city=input("Enter city: ")  #take input city
    stu[name]=city              #key and value

print("Names:")     #displaay names
for name in stu.keys():  #namees are stored as keys
    print(name)

print("Cities:")   #display city name
for city in stu.values():  #city are stored as value
    print(city)

print("Student name and city:")   #display both city and name
for name, city in stu.items():
    print(name, "-", city)

countcity = {}   #dict to count and store city

for city in stu.values():   #city are stored as value
    if city in countcity:
        countcity[city] += 1  #increase count
    else:
        countcity[city] = 1

print("Number of students in each city:")
for city, count in countcity.items():
    print(city, "=", count)
