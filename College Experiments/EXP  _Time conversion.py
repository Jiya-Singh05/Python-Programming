#converting time
sec=int(input("Enter seconds:"))
hour=sec//3600
sec=sec%3600
mins=sec//60
sec=sec%60

print("Hours:",hour)
print("Minutes:",mins)
print("Seconds:",sec)
