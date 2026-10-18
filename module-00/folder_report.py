from pathlib import Path


def scan_folder(folder):
    counts = {} 
    total_size = 0
    for item in folder.iterdir():
        if item.is_file():
            suf = item.suffix
            total_size = total_size + item.stat().st_size
            if suf not in counts:
                counts[suf] = 0
        
            counts[suf] = counts[suf] + 1 
    return counts, total_size                
folder_name = input("Please, Select a Folder: ")
folder = Path(folder_name)
try: 
    counts, num_sum = scan_folder(folder)
    print(counts)
    print("Total:", num_sum)
except FileNotFoundError:
    print("Folder not found:", folder_name)

