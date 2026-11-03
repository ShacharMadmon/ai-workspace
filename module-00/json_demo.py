import json
from pathlib import Path

text = Path("module-00/tasks.json").read_text()
data = json.loads(text)

print(type(data))
print(data[0])
print(data[0]["title"])

new_text = json.dumps(data, indent=4)
print(new_text)
print(type(new_text))
Path("module-00/tasks.json").write_text(new_text)