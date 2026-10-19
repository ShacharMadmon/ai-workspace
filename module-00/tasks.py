from dataclasses import dataclass


@dataclass
class Task:
    title: str
    priority: int
    done: bool = False


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add(self, title, priority):
        self.tasks.append(Task(title, priority))
        


manager = TaskManager()
manager.add("Buy milk", 1)
manager.add("Cook lunch", 2)
print(manager.tasks)
