# que 2 
f=open("numberexp8.txt","r")     #reading file
a=f.read()
f.close()

numbers=list(map(int, a.split()))  #converting the string in the file to integers
maxnum=max(numbers)                ##finding maximum number using inbuilt max function
print("maximum number is :", maxnum)  #printing max number
avg = sum(numbers) / len(numbers)     #finding average number by dividing sum with total  numbers of int
print("Average:", avg)    #printing avg 

count = 0            #initializing count=0 to count numbers greater than 100
for i in numbers:
    if i > 100:     #applying condition to check >100
        count += 1    #increasing count if >100
print("Numbers greater than 100 are:",count)     #print 
