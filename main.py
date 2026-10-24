tasks = []

while True:
    print("\nWelcome to TaskTracker!")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added succefully!")

    elif choice == "2":
        print("Your tasks:")

        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1, 2, or 3.")