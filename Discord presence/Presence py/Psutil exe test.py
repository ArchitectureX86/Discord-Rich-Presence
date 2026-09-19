# Psutil stuff, to find an exe.
import os
import psutil

process_name = "Peach Dungeon.exe"
for p in psutil.process_iter(['name']):
        if p.info['name'] == process_name:
            print(process_name)
        else:
                print("FUCK!")
