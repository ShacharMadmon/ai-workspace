from dataclasses import dataclass


@dataclass(slots=True)
class Task:
    title: str
    priority: int
    done: bool = False


def get_priority(task):
    return task.priority


def get_title(task):
    return task.title


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add(self, title, priority):
        if priority > 5 or priority < 1:
            raise ValueError("Priority must be between 1 and 5")
        self.tasks.append(Task(title, priority))

    def open_tasks(self):
        result = []
        for task in self.tasks:
            if task.done == False:
                result.append(task)
        return result
    
    def done_tasks(self):
        result = []
        for task in self.tasks:
            if task.done:
                result.append(task)
        return result
    
    def urgent_tasks(self):
        result = []
        for task in self.tasks:
            if task.priority == 1:
                result.append(task)
        return result
    
    def tasks_by_priority(self, level):
        result = []
        for task in self.tasks:
            if task.priority == level:
                result.append(task)
        return result
    
    def open_titles(self):
        result = []
        for task in self.tasks:
            if task.done == False:
                result.append(task.title)
        return result
    
    def at_least(self, level):
        result = []
        for task in self.tasks:
            if task.priority >= level:
                result.append(task)
        return result
    
    def count_open(self):
        return len(self.open_tasks())
    
    def complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.done = True
                return
        raise ValueError("Task not found: " + title) 
    
    def set_priority(self, title, new_priority):
        if new_priority > 5 or new_priority < 1:
            raise ValueError("Priority must be between 1 and 5")            
        for task in self.tasks:
            if task.title == title:
                task.priority = new_priority
                return
        raise ValueError("Task not found: " + title) 
         
    def remove(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                return
        raise ValueError("Task not found: " + title)
    
    def sorted_by_priority(self):
        return sorted(self.tasks, key=get_priority)
    
    def sorted_by_title(self):
        return sorted(self.tasks, key=get_title)
    
    def sorted_by_priority_desc(self):
        return sorted(self.tasks, key=get_priority, reverse = True)
    
    def open_sorted(self):
        return sorted(self.open_tasks(), key=get_priority)
    
    
manager = TaskManager()
manager.add("Buy milk", 1)
manager.add("Cook lunch", 2)
manager.add("Pay bills", 1)
manager.add("Call mom", 3)
manager.add("Read book", 5)
manager.tasks[0].title = "Buy bread"


try:
    manager.add("Oops", 99)
except ValueError:
    print("Priority must be between 1 and 5")
manager.tasks[0].done = True
print("Open:", manager.open_tasks())
print("Done:", manager.done_tasks())
print("Urgent:", manager.urgent_tasks())
print("Priority 1:", manager.tasks_by_priority(1))
print("Priority 2:", manager.tasks_by_priority(2))
print("Priority 3:", manager.tasks_by_priority(3))
print("Priority 5:", manager.tasks_by_priority(5))
print("Open titles:", manager.open_titles())
print("At least 3:", manager.at_least(3))
print("Open count:", manager.count_open())
manager.complete("Call mom")
try:
    manager.complete("Fly to Mars")
except ValueError as e:
    print(e)    
try:
    manager.set_priority("Call mom",4)
    manager.set_priority("Call mon",7)
except ValueError as f:
    print(f)
print("Done:", manager.done_tasks())
manager.remove("Read book")
print("After remove:", manager.open_titles())
try:
    manager.remove("Read book")
except ValueError as e:
    print(e)
print("Original:", manager.tasks)
print("Sorted:", manager.sorted_by_priority())
print("Sorted by Title:", manager.sorted_by_title())
print("Desc.Sorted:", manager.sorted_by_priority_desc())
print("Open Sorted:", manager.open_sorted())