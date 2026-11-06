import csv
from pathlib import Path

text = Path("module-00/expenses.csv").read_text()
lines = text.splitlines()
reader = csv.DictReader(lines)

for record in reader:
    if record["paid"] == "True":
        print(record["description"], "is paid")
    