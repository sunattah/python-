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
    elif choice == "2":
        if len(tasks) == 0:
            print("no task yet")
        else:
            for num, task in enumerate(tasks, start=1):
                print(f"{num}. {task}")
    elif choice == "3": 
        if not tasks:
            print("Nothing to delect")
        else:
            for num, task in enumerate(tasks, start=1):
                print(f"{num}. {task}")
        try:
            input_del = int(input("enter task to delect:  "))
            if 1 <= 1 and input_del <= len(tasks):
                removed =tasks.pop(input_del-1)
                print(f"delected {removed}")
            else:
                print("Invlid number")
        except ValueError:
                print("invalid number")

        # del_tas = input("input the value to be delected:  ")
        # tasks.append(del_tas)
       
    

        
    elif choice == "4":
        print("good bye and thank you")
        break
    else:
        print("invalid option")