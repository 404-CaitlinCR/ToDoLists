tasks = []

def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def listTask():
    if not tasks:
        print("There are no tasks in the list")
    else:
        print("Current Tasks: ")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")
            

def deleteTask():
    listTask()
    try:
        taskToDelete = int(input("Enter number of task to remove"))
        if taskToDelete >=0 and taskToDelete < len(tasks):
            ### ,pop lets you specify the index of what we want to delete
            tasks.pop(taskToDelete)
            print(f"Task '{taskToDelete}' was removed from list")
        else:
            print(f"Task #{taskToDelete} not found")
    except:
        print(f"Task '{taskToDelete}' does not exist on list")


if __name__ == "__main__":
    print("Welcom to the to do list app! ")
    while True:
        print("\n")
        print("Please select one of the follwoing options")
        print("------------------------------------------")
        print("1. Add new task")
        print("2. Delete a task")
        print("3. List task")
        print("4. Quit")

        choice = input("Enter you choice: ")

        if (choice == '1'):
            addTask()
        elif (choice == '2'):
            deleteTask()
        elif (choice == '3'):
            listTask()
        elif (choice == '4'):
            break
        else:
            print("Invalid input, try again.")
        
        print("Goodbye!")
        pass