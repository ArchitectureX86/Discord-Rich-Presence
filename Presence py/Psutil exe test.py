# Psutil stuff, to find an exe.
import psutil

process_name = "Peach Dungeon.exe"
for p in psutil.process_iter(['name']):
        if p.info['name'] == process_name:
            print(process_name)
        else:
            pass