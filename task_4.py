new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

# задание 1
completed_tasks.append(new_tasks.pop(4))

# задание 2
new_tasks.remove('task_007')

# задание 3
print(new_tasks[len(new_tasks)-1])