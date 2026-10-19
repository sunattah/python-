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
        pass
    elif choice == "3":
        if len(tasks) == 0:
            print("Nothing to delete.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Deleted: {removed}")
        else:
            print("Invalid number.")

    # elif choice == "4":
    #     print("Goodbye!")
    #     break
    # else:
    # print("Invalid choice, try again.")