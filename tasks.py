# TASKS MODULE
# This module contains the core functions for managing tasks, including creating, listing, completing, and deleting tasks. It interacts with the storage module to load and save tasks from a file.

# We import the load_tasks and save_tasks functions from the storage module to handle reading and writing tasks to a file. We also import datetime to add timestamps to our tasks when they are created.
from storage import load_tasks, save_tasks
from datetime import datetime

# The create_task function takes a title and an optional description to create a new task. It loads the existing tasks, creates a new task with a unique ID, and saves the updated list of tasks back to the file. It also prints a success message to the user.
def create_task(title, description=""):
    
    # We load the existing tasks from the file using the load_tasks function. Then we create a new task as a dictionary with an ID (which is one more than the current number of tasks), the title, description, a done status set to False, and a created_at timestamp. We append this new task to the list of tasks and save it back to the file using the save_tasks function. Finally, we print a message confirming that the task was created successfully.
    tasks = load_tasks()
    
    # We create a new task as a dictionary with the following keys
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "done": False,
        "created_at": datetime.now().strftime("%d/%m/%Y %H:%M")
    }
    
    # We append the new task to the list of tasks and save it back to the file using the save_tasks function. Finally, we print a message confirming that the task was created successfully.
    tasks.append(task)
    
    # We save the updated list of tasks back to the file using the save_tasks function. Finally, we print a message confirming that the task was created successfully.
    save_tasks(tasks)
    
    # Finally, we print a message confirming that the task was created successfully.
    print(f"Task '{title}' created successfully!")


# In this function, we load the existing tasks and check if there are any tasks to display. If there are no tasks, we print a message indicating that no tasks were found. If there are tasks, we loop through each task and print its details, including the status (done or not), ID, title, creation date, and description (if it exists).
def list_tasks():
    
    # First, we load the existing tasks from the file using the load_tasks function. 
    tasks = load_tasks()
    
    # We check if there are any tasks to display. If there are no tasks, we print a message indicating that no tasks were found. If there are tasks, we loop through each task and print its details, including the status (done or not), ID, title, creation date, and description (if it exists).
    if not tasks:
        print("No tasks found.")
        return
    
    # If the user wants to filter the tasks, we ask for the filter type (pending or completed) and create a new list of tasks based on that filter. If the user chooses "pending", we create a list of tasks that are not done. If the user chooses "completed", we create a list of tasks that are done. If there are no tasks that match the filter, we print a message indicating that no tasks were found for that filter.
    if filter == "pending":
        tasks = [t for t in tasks if not t["done"]]
    elif filter == "completed":
        tasks = [t for t in tasks if t["done"]]
    
    if not tasks:
        print("No tasks found for this filter.")
        return
    
    # We loop through each task in the list of tasks and print its details. We use a checkmark (✔) to indicate that a task is done and a cross (✘) to indicate that it is not done. We also print the ID, title, creation date, and description (if it exists) for each task.
    for task in tasks:
        status = "✔" if task["done"] else "✘"
        print(f"[{status}] #{task['id']} - {task['title']} ({task['created_at']})")
        if task["description"]:
            print(f"     {task['description']}")


# The complete_task function takes a task ID as an argument, loads the existing tasks, and marks the task with the given ID as completed (done = True). It then saves the updated list of tasks back to the file and prints a success message. If the task with the given ID is not found, it prints an error message.
def complete_task(task_id):
    tasks = load_tasks()
    
    # We loop through the list of tasks to find the task with the given ID. If we find it, we set its "done" status to True, save the updated list of tasks back to the file using the save_tasks function, and print a message confirming that the task was marked as completed. If we finish looping through the tasks without finding a task with the given ID, we print an error message indicating that the task was not found.
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            print(f"Task #{task_id} marked as completed!")
            return
    print(f"Task #{task_id} not found.")


# The delete_task function takes a task ID as an argument, loads the existing tasks, and removes the task with the given ID from the list. It then saves the updated list of tasks back to the file and prints a success message. If the task with the given ID is not found, it prints an error message.
def delete_task(task_id):
    tasks = load_tasks()
    
    # We create a new list of tasks that includes all tasks except the one with the given ID. If the length of the new list is the same as the original list, it means that no task with the given ID was found, and we print an error message. If a task was removed, we save the updated list of tasks back to the file using the save_tasks function and print a message confirming that the task was removed.
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print(f"Task #{task_id} not found.")
        return
    save_tasks(new_tasks)
    print(f"🗑 Task #{task_id} removed.")