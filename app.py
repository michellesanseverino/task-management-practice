# APP.PY
# This is the entry point for the web app. It uses Flask to create a web server

# Importing the necessary modules and functions. We import Flask and related functions from the flask module to create our web app and handle requests. We also import the functions from the tasks module that we will use to manage our tasks.
from flask import Flask, render_template, request, redirect, url_for
from tasks import get_tasks, create_task, complete_task, delete_task

# We create an instance of the Flask class, which will be our web application. We then define routes for the different pages and actions in our app, such as displaying the task list, creating a new task, completing a task, and deleting a task. Each route is associated with a function that handles the logic for that route. Finally, we run the app in debug mode so that we can see any errors that occur during development.
app = Flask(__name__)


# We define the route for the home page ("/") which will display the list of tasks. We also handle an optional filter parameter in the URL to allow users to filter tasks by their status (pending or done). The function retrieves the tasks based on the filter and renders the "index.html" template, passing the tasks and the current filter to the template for rendering.
@app.route("/")
def index():
    filter = request.args.get("filter", None)  # pega o filtro da URL
    tasks = get_tasks(filter)
    return render_template("index.html", tasks=tasks, filter=filter)

# We define the route for creating a new task ("/create") which accepts POST requests. The function retrieves the title and description from the form data, creates a new task using the create_task function, and then redirects the user back to the home page to see the updated list of tasks.
@app.route("/create", methods=["POST"])
def create():
    title = request.form.get("title")
    description = request.form.get("description", "")
    if title:
        create_task(title, description)
    return redirect(url_for("index"))

#  Defining the route for completing a task ("/complete/<int:task_id>") which accepts GET requests. The function takes the task ID from the URL, marks the task as completed using the complete_task function, and then redirects the user back to the home page to see the updated list of tasks.
@app.route("/complete/<int:task_id>")
def complete(task_id):
    complete_task(task_id)
    return redirect(url_for("index"))


# Calling the delete_task function with the task ID from the URL to delete a task, and then redirecting the user back to the home page to see the updated list of tasks.
@app.route("/delete/<int:task_id>")
def delete(task_id):
    delete_task(task_id)
    return redirect(url_for("index"))


# This block checks if the script is being run directly (as the main program) and if so, it starts the Flask development server in debug mode. This allows us to see any errors that occur during development and automatically reload the server when we make changes to the code.
if __name__ == "__main__":
    app.run(debug=True)