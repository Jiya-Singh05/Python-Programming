# Create a Todo list Manager where users can add, view, and remove tasks. Use List for storing tasks. 
tasks = []

while True:
    print("\n TO DO LIST MANAGER")
    print("1. ADD TASK")
    print("2. VIEW TASK")
    print("3. REMOVE TASK")
    print("4. EXIT")

    choice = int(input("Enter your choice (1-4): "))
    
    if choice == 1:
        task = input("Enter task to add: ").split()
        tasks.append(task)
        print("Task added successfully!")
    elif choice == 2:
        if len(tasks) == 0:
            print("List is empty")
        else:
            print("To do list:\n", tasks)
    elif choice == 3:
        rem = input("Enter task to remove: ")
        if rem in tasks:
            tasks.remove(rem)
            print("After remove:", tasks)
        else:
            print("Item not found")
    elif choice == 4:
        break
    else:
        print("Invalid input")
