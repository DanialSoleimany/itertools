import itertools

team = ['Alice', 'Bob', 'Charlie']

tasks = ['Task 1', 'Task 2', 'Task 3', 'Task 4', 'Task 5']

cycled_team = itertools.cycle(team)

assigned_tasks = {}

for task in tasks:
    member = next(cycled_team)
    if member in assigned_tasks:
        assigned_tasks[member].append(task)
    else:
        assigned_tasks[member] = [task]

for member, tasks in assigned_tasks.items():
    print(f"{member} is assigned: {', '.join(tasks)}")
