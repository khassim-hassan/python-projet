class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if task:
            self.tasks.append({"task": task, "completed": False})

    def delete_task(self, task):
        self.tasks = [t for t in self.tasks if t["task"] != task]

    def complete_task(self, task):
        for t in self.tasks:
            if t["task"] == task:
                t["completed"] = True
