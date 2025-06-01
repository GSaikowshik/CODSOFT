tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task():
    view_tasks()
    if tasks:
        try:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Task '{removed}' deleted!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        print("\nTo-Do List Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
