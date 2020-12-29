import os.path

for entry in os.scandir():
    try:
        if entry.is_file and entry.name.endwith('.py'):
            print(entry.name)

    except Exception as e:
        print("dd")