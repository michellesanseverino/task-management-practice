# MAIN.PY
# This is the entry point for the app. It shows the menu for the user and calls the appropriate functions from the tasks module based on the user's choice.

# Here we import the functions from the tasks module that we will use in this file.
from tasks import create_task, list_tasks, complete_task, delete_task

# This function displays the menu options to the user.
def menu():
    print("\n=== Tasks Manager ===")
    print("1. List all tasks")
    print("2. Create task")
    print("3. Complete task")
    print("4. Delete task")
    print("0. Exit")

# This is the main function that runs the app. It shows the menu and handles the user's input to call the appropriate functions from the tasks module.
def main():
    while True:
        # Show the menu and get the user's choice
        menu()
        option = input("\nChoose an option: ").strip()
        
        # Based on the user's choice, call the appropriate function from the tasks module
        # We use if-elif statements to check the user's input and call the corresponding function. If the user chooses to exit, we break the loop and end the program. If the user enters an invalid option, we print an error message.
        # Note: We also handle the input for creating a task, completing a task, and deleting a task by asking the user for the necessary information (like title, description, or task ID) and passing that information to the respective functions.
        
        # If option is "1", we call the list_tasks function to display all tasks.
        if option == "1":
            print("\n=== Filter by: ===")
            print("1. All tasks")
            print("2. Pending tasks")
            print("3. Completed tasks")
            filter = input("Choose filter: ").strip()
            
            if filter == "1":
                list_tasks()
            elif filter == "2":
                list_tasks(filter="pending")
            elif filter == "3":
                list_tasks(filter="done")
            else:
                print("Invalid filter option. Showing all tasks.")
            
            list_tasks(filter)

        # If user chooses "2", we ask for the title and description of the new task and call the create_task function to add it to the list.
        elif option == "2":
            title = input("Title: ").strip()
            description = input("Description (optional): ").strip()
            create_task(title, description)

        # If user chooses "3", we ask for the ID of the task they want to mark as completed and call the complete_task function with that ID.
        elif option == "3":
            task_id = int(input("Task ID: "))
            complete_task(task_id)

        # If user chooses "4", we ask for the ID of the task they want to delete and call the delete_task function with that ID.
        elif option == "4":
            task_id = int(input("Task ID: "))
            delete_task(task_id)

        # If user chooses "0", we print a goodbye message and break the loop to exit the program.
        elif option == "0":
            print("See you later!")
            break

        # If the user enters an option that is not valid (not "1", "2", "3", "4", or "0"), we print an error message indicating that the option is invalid.
        else:
            print("Invalid option.")

# Finally, we check if this file is being run as the main program (as opposed to being imported as a module in another file). If it is, we call the main() function to start the app.
if __name__ == "__main__":
    main()