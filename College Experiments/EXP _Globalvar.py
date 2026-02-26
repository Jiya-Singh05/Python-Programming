#global variable
def f1 ():
    global x
    x=int(input("enter value for x:"))
    print(f"Inside func value:{x}")
f1()
print(f"Outside func value:{x}")
