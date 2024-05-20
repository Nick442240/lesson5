class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.is_completed = False

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].is_completed = True

    def get_all_tasks(self):
        return self.tasks

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task.is_completed]


task_manager = TaskManager()
task_manager.add_task("Приготовить удочки", "2024-05-21")
task_manager.add_task("Сделать презентацию", "2024-05-22")
task_manager.add_task("Выполнить ДЗ", "2024-05-23")

task_manager.mark_task_completed(0)

all_tasks = task_manager.get_all_tasks()
for task in all_tasks:
    status = "Выполнено" if task.is_completed else "В работе"
    print(f"Description: {task.description}, Срок: {task.deadline}, Статус: {status}")
