from datetime import datetime
from validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    validate_task_title(title)
    validate_task_description(description)
    validate_due_date(due_date)
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, task_list=None):
    if task_list is None:
        task_list = tasks
    if 0 <= index < len(task_list):
        task_list[index]["completed"] = True
        print("Task marked as complete!")
    else:
        raise IndexError("Task index out of range.")
    
# Implement view_pending_tasks function
def view_pending_tasks(task_list=None):
    if task_list is None:
        task_list = tasks
    if not task_list:
        print("No pending tasks.")
        return
    for i, task in enumerate(task_list, 1):
        status = "✓" if task["completed"] else "○"
        print(f"{i}. [{status}] {task['title']} - Due: {task['due_date']}")

# Implement calculate_progress function
def calculate_progress(task_list=None):
    if task_list is None:
        task_list = tasks
    if not task_list:
        return 0
    completed = sum(1 for task in task_list if task["completed"])
    progress = (completed / len(task_list)) * 100
    return round(progress, 2)