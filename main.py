tasks = []

def add_task(task):
    tasks.append(task)

def view_tasks():
    for task in tasks:
        print(task)

add_task("Learn Python")
add_task("Build API")

view_tasks()
