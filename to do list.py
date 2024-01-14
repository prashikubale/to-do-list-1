def display_menu():
    print("Todo List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list.append({"task": task, "completed": False})
    print("Task added successfully!")

def view_tasks(todo_list):
    if not todo_list:
        print("No tasks in the todo list.")
    else:
        print("Todo List:")
        for index, task in enumerate(todo_list, start=1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{index}. {task['task']} - {status}")

def mark_completed(todo_list):
    view_tasks(todo_list)
    try:
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_index < len(todo_list):
            todo_list[task_index]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def main():
    todo_list = []

    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            add_task(todo_list)
        elif choice == 2:
            view_tasks(todo_list)
        elif choice == 3:
            mark_completed(todo_list)
        elif choice == 4:
            print("Exiting the Todo List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
