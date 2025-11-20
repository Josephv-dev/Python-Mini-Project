import os
import datetime
import csv
import sys
import json

# file too store all the task
FILE_NAME = "tasks.txt"
def new_func():
    DATE_FORMAT = "%Y-%m-%d, %H:%M"
    return DATE_FORMAT

DATE_FORMAT = new_func()

#  Load tasks from file
def load_file():
    tasks = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                task_id, title, status, deadline = line.strip().split(" | ")
                tasks[int(task_id)] = {"title": title, "status": status, "deadline": deadline}
                
    return  tasks

"""Since task is now the inner dictionary, you must use square brackets [] and the key (which is a string like 'status' or 'title') to get the data you wan"""
# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task_id, task  in tasks.items():
            file.write(f"{task_id} | {task['title']} | {task['status']} | {task['deadline']}\n")
            
# Add a new task

def add_task(tasks, title = None, deadline = None):
    if title is None:
        title = input("Enter task title: ")
    if deadline is None:
        deadline = input("Enter a deadline for the task (e.g, YYYY-MM-DD, H-M): ")
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {"title": title, "status": "incomplete", "deadline":deadline}
    print(f"Task'{title}'added {deadline}.")
    


#View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks avaliable.")
    else:
        
        today = datetime.datetime.now()
        for task_id, task in tasks.items():
            deadline_date = datetime.datetime.strptime(task["deadline"], DATE_FORMAT)
            #Check if overdue: compare deadline_dt < now
            is_overdue = (task['status']) == 'incomplete' and deadline_date < today
            #use ternary operator to show overdue tasks
            warning = " (OVERDUE)" if is_overdue else ""
            print(f"[{task_id}] {task['title']} - {task['status']} - {task['deadline']}{warning}")

# Mark task as complete
def complete_task(tasks, task_id = None):
    try:
        if task_id is None:
            task_id = int(input("Enter task ID to mark as complete: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    if task_id in tasks:
        tasks[task_id]["status"] = "complete"
        print(f"Task '{tasks[task_id]['title']}' marked as complete.")
    else:
        print("Task not found.")
        

#Export task to CSV(comma seperated values)
def export_tasks_csv(tasks):
    with open("tasks_export.csv", "w", newline='') as csvfile:
        """newline='' argument prevents the writer from adding extra blank rows between your data, which is a common issue when writing CSV files in Python."""
        writer = csv.writer(csvfile)
        writer.writerow(["Task ID", "Title", "Status", "Deadline"])
        for task_id, task in tasks.items():
            writer.writerow([task_id, task["title"], task["status"], task["deadline"]])
        
# Export task to JSON
def export_tasks_json(tasks):
    with open("tasks_export.json", "w") as jsonfile:
        list_new = []
        for task_id, task in tasks.items():
            data = {
                "Task ID" : task_id, 
                "title" : task["title"], 
                "status" : task["status"], 
                "deadline" : task["deadline"]
            }
            
            list_new.append(data)
        json.dump(tasks, jsonfile, indent=4)

# delete task
def delete_task(tasks, task_id = None):
    if task_id is None:
        try:
            task_id = int(input("Enter task ID to delete: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
    if task_id in tasks:
        deleted_task = tasks.pop(task_id)
        print(f"Task '{deleted_task['title']}' deleted.")
    else:
        print("Task not found.")
        

# Main Menu
def main():
    tasks = load_file()
    
    #command line argument
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "add_task":
            if len(sys.argv) < 4:
                print("Usage: python script add_task <title> <deadline>")
            else:
                print("Added task via command line")
                title = sys.argv[2]
                deadline = sys.argv[3]
                
                add_task(tasks, title, deadline)
                save_tasks(tasks)
                return
        elif command == "Complete task":
            if len(sys.argv) < 3:
                print("Usage:python script complete_task <task_id>")
            else:
                task_id = int(sys.argv[2])
                complete_task(tasks, task_id)
                save_tasks(tasks)
                return
        elif command == "view_tasks":
            view_tasks(tasks)
            return
        elif command == "delete_task":
            if len(sys.argv) < 3:
                print("Usage: python script delete_task <task_id>")
            else:
                task_id = int(sys.argv[2])
                delete_task(tasks, task_id)
                save_tasks(tasks)
                return
        else:
            print("Unknown command.")
    
#------------------------------------------------------
# INTERACTIVE MODE
#------------------------------------------------------        
            
    else:
        while True:
            print("\nTask Manager")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Complete")
            print("4. Delete Task")
            print("5. Export Tasks to CSV")
            print("6. Export Tasks to JSON")
            print("7. Exit")
            choice = input("Enter your choice: ")
            
            if choice == "1":
                add_task(tasks)
            elif choice == "2":
                view_tasks(tasks)
            elif choice == "3":
                complete_task(tasks)
            elif choice == "4":
                delete_task(tasks)
            elif choice == "5":
                export_tasks_csv(tasks)
                print("Tasks exported to tasks_export.csv")
            elif choice == "6":
                export_tasks_json(tasks)
                print("Task exported to tasks_export.json")
            elif choice == "7":
                save_tasks(tasks)
                print("Exiting Task Manager.")
                break
            else:
                print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
    