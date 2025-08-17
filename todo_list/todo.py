from pandas import DataFrame, read_csv, to_csv
from InquirerPy import inquirer, prompt

files = []
continue_ = True

def add_task():
    fileName = inquirer.select(
        message = "Select existing todo list: ",
        choices = files,
    )
    task = inquirer.text(message="Enter the task to add:")
    due = inquirer.text(message="Enter the due date (YYYY-MM-DD):")
    new_data = DataFrame([{"task": task, "due": due}])
    new_data.to_csv(fileName, mode='a', header=False, index=False)
    print("Task added successfully!")

def create_list():
    fileName = inquirer.text(message="Choose a file name: ")
    task = inquirer.text(message="Enter inital task: ")
    due = inquirer.text(message="Enter the due date (YYYY-MM-DD):")
    data = DataFrame([{"task": task, "due": due}])
    data.to_csv(fileName, index=False)
    print(f"Todo list '{fileName}' created successfully!")
    files.append(fileName)
    return fileName

def view_list():
    fileName = inquirer.select(
        message = "Select todo list to view: ",
        choices = files,
    )
    data = read_csv(fileName)
    if data.empty:
        print("The todo list is empty.")
    else:
        print(data)

def main():
    action = inquirer.select(
        message="What would you like to do?",
        choices=["Add a task", "Create a new todo list", "View existing todo list", "Exit"],
    ).execute()

    if action == "Add a task":
        if not files:
            print("No todo lists available. Please create one first.")
            return
        add_task()
    elif action == "Create a new todo list":
        create_list()
    elif action == "View existing todo list":
        if not files:
            print("No todo lists available. Please create one first.")
            return
        view_list()
    elif action == "Exit":
        print("Goodbye!")
        continue_ = False
        return
    
while continue_:
    main()