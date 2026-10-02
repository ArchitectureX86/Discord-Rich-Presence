from pypresence import Presence
from pypresence.types import ActivityType, StatusDisplayType
import pypresence
import time
import psutil
import platform
import os
import socket

Git = "https://raw.githubusercontent.com/ArchitectureX86/Discord-Rich-Presence/refs/heads/main/Discord%20presence/assets/"
PyPi = "https://pypi.org/project/"
SysInfo = f"{platform.system()} {platform.release()} {os.name}"
SysName = f"{socket.gethostname()}"
SysUser = f"{os.environ.get("USERNAME", "Unknown user")}"
PyVer = f"🐍v{platform.python_version()}"
PypVer = f"PyPresence v{pypresence.__version__}"
PsuVer = f"Psutil v{psutil.__version__}"
DualVer = f"{PypVer} | {PsuVer}"

client_id = "1546844285645627542"
RPC = Presence(client_id)
RPC.connect()

start_time = (time.time())

print("restart")

while True:
    process_name = "Peach Dungeon.exe"
    for p in psutil.process_iter(['name']):
        if p.info['name'] == process_name:
            limage = "https://img.itch.zone/aW1nLzE4ODUxNTI2LnBuZw==/original/Ky7EVY.png"
            xname = (process_name[:-4])
            xbuttons = [{'label': f'{xname} on itch.io', 'url': 'https://itch.io'}]
            break
        else:
            limage = f"{Git}Desktop.png"
            xname = "No itch.io game running."
            xbuttons = [{'label': 'google.com', 'url': 'https://google.com'}]
# Show as "Playing"
    RPC.update(
            large_image = limage,
            large_text = f"{SysName}.",
            name = f"{xname}.",
            details = f"{PyVer}",
            state = f"{PsuVer}",
            start = int(start_time),
            buttons = xbuttons
            )

    time.sleep(5)