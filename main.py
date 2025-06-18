def add_task(task_name, tasks):
    task = {"Task": task_name, "Completed": False}
    tasks.append(task)
    print(f"Task {task_name} was successfully added")
    return

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

    if choice == "6":
        break

print("Program Finished")