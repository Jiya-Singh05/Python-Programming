# Create a Todo list Manager where users can add, view, and remove tasks. Use List for storing tasks. 
todo=[]
def add():
    task=input("Enter the task: ")
    todo.append(task)
    print("Task added")
    
def delete():
  task=input("Enter the task to delete: ")
  if task in todo:
        todo.remove(task)
        print("Task deleted successfully.")
  else:
        print("Task not found.") 
        
def display():
    if len(todo)==0:
        print("No tasks in the to-do list.")
    else:
        print(todo)

choice=1
print(" 1].Add task\n 2].Delete task\n 3].Display tasks\n 4].Exit")
while(choice!=4):
    choice=int(input("Enter choice:\n"))
    if(choice==1):
        add()
    elif(choice==2):
        delete()
    elif(choice==3):
        display()
    else:
        break
               
