#Highest, lowest and avg sum
l=[]
n=int(input("Enter total number of score: "))
for i in range (n):
    a=float(input("Enter score: "))
    l.append(a)
x=max(l)
y=min(l)
print(f"Max:{x} and Min:{y}")
length=len(l)
avg=sum(l) / length
print(f"Avg score:{avg}")
