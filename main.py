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
        print("No tasks avaiable")

def update_tasks(tasks):
    counter = 1
    for task in tasks:
        print(f"{counter}. {task["Task"]}")
        counter += 1
    if not tasks:
        print("No tasks avaiable to change")
    choice = int(input("Which task would you like to change? "))
    while choice < 1 and choice >= len(tasks):
        choice = int(input("Insert a valid number: "))
        
    new_task = input("Type the new task: ")

    tasks[choice - 1]["Task"] = new_task

tasks = []


while True:
    print("\nTask manager menu:")
    print("1. Add task")
    print("2. See tasks")
    print("3. Update task")
    print("4. Complete task")
    print("5. Delete completed tasks")
    print("6. Leave")

    choice = input("Type your choice: ")

    if choice == "1":
        task_name = input("Name the task you want to add: ")
        add_task(task_name, tasks)
    elif choice == "2":
        see_tasks(tasks)
    elif choice == "3":
        update_tasks(tasks)
    elif choice == "6":
        break

print("Program Finished")