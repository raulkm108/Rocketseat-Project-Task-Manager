def add_task(task_name, tasks):
    task = {"Task": task_name, "Completed": False}
    tasks.append(task)
    print(f"Task \"{task_name}\" was successfully added")
    return

def see_tasks(tasks):
    print()
    for task in tasks:
        print(f"{task["Task"]}")
    if not tasks:
        print("\nNo tasks avaiable")

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
    elif choice == "6":
        break

print("Program Finished")