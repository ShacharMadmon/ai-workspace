from pathlib import Path
counts = {}
num_sum = 0
folder_name = input("Please, Select a Folder: ")
folder = Path(folder_name)
try: 
    for item in folder.iterdir():
        if item.is_file():
            suf = item.suffix
            num_sum = num_sum + item.stat().st_size
            if suf not in counts:
                counts[suf] = 0
        
            counts[suf] = counts[suf] + 1  

    print(counts)
    print("Total:", num_sum)
except FileNotFoundError:
    print("Folder not found:", folder_name)

