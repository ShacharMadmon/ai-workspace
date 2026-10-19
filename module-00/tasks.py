from dataclasses import dataclass


@dataclass
class Task:
    title: str
    priority: int
    done: bool = False


tasks = []
tasks.append(Task("Buy milk",1,True))
tasks.append(Task("Fix the car",2))
tasks.append(Task("Cook Lunch",3))


for task in tasks:
    if task.done is False:
        print(task.title, task.priority)

