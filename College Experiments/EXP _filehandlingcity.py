#que 3. Assume a file city.txt with details of 5 cities in given format (cityname population(in lakhs) area(in sq KM) ): Display details of all cities 
# Display city names with population more than 10Lakhs 
# Display sum of areas of all cities 

f=open("cityexp8.txt","r")     #reading file
a=f.readlines()    #reading lines
f.close()
totalarea=0  #let total area be 0

print("Details of all cities:")
for line in a:
    b=line.split()   #splitting each line into list city, population and area
    city=b[0]        #city name is stored at index 0 in list
    population=float(b[1])   #population is stored at index 1 in list and converting it to float using conversion
    area= float(b[2])    #area is stored at index 2 in list and converting it to float using conversion
    print(f"City: {city}, Population: {population}, Area: {area}")   #printing city details
    totalarea += area     #adding area of each city to total area

print("Cities with population more than 10 lakhs:")
for line in a:    #tchecking each line again to check population condition
    b=line.split()   #splitting each line into list city, population and area
    city=b[0]       #city name is stored at index 0 in list
    population=float(b[1])    #population is stored at index 1 in list and converting it to float using conversion
    if population > 10:
        print(city)          #checking condition and printing city name if population is more than 10 lakh

print(f"Total area of all cities: {totalarea}")

