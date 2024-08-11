def display_tasks(tasks):
    if not tasks:
        print("No Task!!!")
    else:
        for i, task in enumerate(tasks,1):
            print(f"{i}. {task}")

def main():
    tasks = []

    while True:
        menu = """
        Select Operation:

        1. Add task
        2. Remove Task
        3. View tasks
        4. Exit
        """
        print(menu)

        choise = input("Enter choice (1/2/3/4): ")



        if choise == '1':
            task = input("Enter task: ")
            tasks.append(task)
        elif choise == '2':
            display_tasks(tasks)
            task_index = int(input('Enter task number to remove: ')) - 1
            if 0 <= task_index < len(tasks):
                tasks.pop(task_index)
            else:
                print('Invalid task number...!')
        elif choise == '3':
            display_tasks(tasks)
        elif choise == "4":
            break
        else:
            prtin("Invalid Number ;D")


if __name__ == "__main__":
    main()
