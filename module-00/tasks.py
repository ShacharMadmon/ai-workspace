from dataclasses import dataclass


@dataclass(slots=True)
class Task:
    title: str
    priority: int
    done: bool = False


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add(self, title, priority):
        if priority > 5 or priority < 1:
            raise ValueError("Priority must be between 1 and 5")
        self.tasks.append(Task(title, priority))
        

manager = TaskManager()
manager.add("Buy milk", 1)
manager.add("Cook lunch", 2)
manager.tasks[0].title = "Buy bread"


try:
    manager.add("Oops", 99)
except ValueError:
    print("Priority must be between 1 and 5")
print(manager.tasks)