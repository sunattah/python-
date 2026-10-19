tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task = input("input the task :  ")
        tasks.append(add_task)
        print("Task is added successfully")
        pass
    elif choice == "2":
        if len(tasks) == 0:
            print("no tasks yet")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        # I will write this
        pass
    elif choice == "3":
        # I will write this
        pass
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")