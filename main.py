def add_task(task_name, tasks):
    task = {"Task": task_name, "Completed": False}
    tasks.append(task)
    print(f"Task \"{task_name}\" was successfully added")
    return

def see_tasks(tasks):
    print("\nTask List:")
    counter = 1
    for task in tasks:
        if task["Completed"]:
            status = "✓"
        else:
            status = " "
        print(f"{counter}. [{status}] {task["Task"]}")
        counter += 1
    if not tasks:
        print("No tasks available")
        return
    return

def update_tasks(tasks):
    counter = 1
    print()
    for task in tasks:
        print(f"{counter}. {task["Task"]}")
        counter += 1
    if not tasks:
        print("\nNo tasks available to change")
        return
    choice = int(input("Which task would you like to change? "))
    # It's worth remembering that the program breaks if the input is not an intereger, if it has a "." and if it is an integer
    # Gonna solve it later
    while choice < 1 or choice > len(tasks):
        choice = int(input("Insert a valid number: "))
        
    new_task = input("Type the new task: ")
    old_task = tasks[choice - 1]["Task"]
    tasks[choice - 1]["Task"] = new_task

    print(f"\nThe task \"{old_task}\" was replaced for \"{new_task}\"")
    return

def complete_tasks(tasks):
    counter = 1
    for task in tasks:
        if task["Completed"]:
            status = "✓"
        else:
            status = " "
        print(f"{counter}. [{status}] {task["Task"]}")
        counter += 1
    if not tasks:
        print("No tasks available")
        return
    
    choice = int(input("\nWhich task would you like to complete? "))
    while choice < 1 or choice > len(tasks):
        choice = int(input("Insert a valid number: "))
    adjusted_index = choice - 1

    if tasks[adjusted_index]["Completed"] == False:
        tasks[adjusted_index]["Completed"] = True 
        Task = tasks[adjusted_index]["Task"]
        print(f"\nThe task \"{Task}\" is now completed")
    else:
        print("\nThis task is already checked")
    return

def remove_tasks(tasks):
    if not tasks:
        return
    choice = int(input("\nWhich task do you want to remove? "))
    while choice < 1 or choice > len(tasks):
        choice = int(input("Insert a valid number: "))
    adjusted_index = choice - 1
    removed_task = tasks[adjusted_index]
    tasks.remove(tasks[adjusted_index])
    
    print(f"\nThe task \"{removed_task["Task"]}\" has been removed")
    return

def remove_completed_tasks(tasks):
    tasks2 = []
    for task in tasks:
        if task["Completed"] == False:
            tasks2.append(task)
    if not tasks:
            print("\nNo tasks Available to remove")
            return tasks2 
    
    print("\nAll completed tasks were removed successfully")
    return tasks2
    
tasks = []


while True:
    print("\nTask manager menu:")
    print("1. Add task")
    print("2. See tasks")
    print("3. Update task")
    print("4. Complete task")
    print("5. Delete specific task")
    print("6. Delete all completed tasks")
    print("7. Leave")

    choice = input("Type your choice: ")

    if choice == "1":
        task_name = input("Name the task you want to add: ")
        add_task(task_name, tasks)
    elif choice == "2":
        see_tasks(tasks)
    elif choice == "3":
        update_tasks(tasks)
    elif choice == "4":
        complete_tasks(tasks)
    elif choice == "5":
        see_tasks(tasks)
        remove_tasks(tasks)
    elif choice == "6":
        tasks = remove_completed_tasks(tasks)
    elif choice == "7":
        break

print("Program Finished")