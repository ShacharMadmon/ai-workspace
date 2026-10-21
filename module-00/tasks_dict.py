tasks = []

tasks.append({"title": "Buy milk", "priority": 1, "done": False})
tasks.append({"title": "Cook lunch", "priority": 2, "done": False})

tasks[0]["titel"] = "Buy bread"

for task in tasks:
    print(task["title"])
    
    
print(tasks[0])