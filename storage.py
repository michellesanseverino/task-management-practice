# Storage.py
# This file contains functions for loading and saving tasks to a JSON file. 

# We import the json module to handle JSON data and the os module to check if the file exists.
import json
import os

# We define a constant FILE that holds the name of the JSON file where we will store our tasks. This makes it easy to change the file name in one place if needed.
FILE = "tasks.json"

# The load_tasks function checks if the tasks file exists. If it does not exist, it returns an empty list. If it does exist, it opens the file, reads the JSON data, and returns it as a Python list of tasks.
def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

# The save_tasks function takes a list of tasks as an argument and saves it to the JSON file. It opens the file in write mode and uses json.dump to write the tasks to the file in a pretty-printed format (with indentation) and ensures that non-ASCII characters are handled correctly.
def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)