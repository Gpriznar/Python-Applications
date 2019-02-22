tasks =[]

def view_all_tasks():
    for index in range(len(tasks)):
        print(f'{index +1} - {tasks[index]["title"]} - {tasks[index]["priority"]}')

def delete_task():
    task_number = int(input("Which task would you like to delete?: ")) -1
    for task in tasks:
        if task_number == tasks.index(task):
            tasks.remove(task)
            print("***The task has been deleted***")

def show_menu():
    print("Press 1 to add a new task: ")
    print("Press 2 to view all tasks: ")
    print("press 3 to delete task")
    print("Press Q to quit: ")

def add_new_task():
    task_name = input("Enter name of task: ")
    task_priority = input("Enter the priority: ")

   # create Dictionary
    task = {"title": task_name, "priority": task_priority}

   # Adding a dictionary to array
    tasks.append(task)

user_input = ""

while user_input != "Q":
    show_menu()
    user_input = input("Enter your choice: ")

    if user_input == "Q":
        print("Goodbye!")
    elif user_input == "1":
        add_new_task()
    elif user_input == "2":
        view_all_tasks()
    elif user_input == "3":
        delete_task()
