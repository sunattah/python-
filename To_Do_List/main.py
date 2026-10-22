tasks = []

while True:
    print()
    print("----To-Do-List----")
    print("1: Add task")
    print("2: View task")
    print("3: Delect task")
    print("4: Exit")
    print()

    choice = input("enter your option: ")
    if choice == "1":
        new_task = input("Enter your task:  ")
        tasks.append(new_task)

        print("task added")
    if choice == "2":
        if tasks == "":
            print("no task yet")
        else:
            for i in enumerate(tasks, start=1):
                print(i)
    if choice == "3":
        if tasks == "":
            print("Nothing to delect")
        
    if choice == "4":
        print("good bye and thank you")
        break
    else:
        print("invalid input")
