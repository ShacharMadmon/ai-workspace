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


def main():
    folder_name = input("Please, Select a Folder: ")
    folder = Path(folder_name)
    try: 
        counts, total_size = scan_folder(folder)
        print(counts)
        print("Total:", total_size)
    except FileNotFoundError:
        print("Folder not found:", folder_name)
    except PermissionError:
        print("No permission to read folder:", folder_name)

if __name__ == "__main__":
    main()