from pathlib import Path
counts = {}
num_sum = 0
folder = Path("module-00")

for item in folder.iterdir():
    if item.is_file():
        suf = item.suffix
        num_sum = num_sum + item.stat().st_size
        if suf not in counts:
            counts[suf] = 0
        
        counts[suf] = counts[suf] + 1  
print(counts)
print("Total:", num_sum)