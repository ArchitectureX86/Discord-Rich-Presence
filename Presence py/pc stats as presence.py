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

while True:
    cpu = f"{int(psutil.cpu_percent(interval=None))}%"
    mem = f"{int(psutil.virtual_memory().percent)}%"
# Show as "Playing"
    RPC.update(
            large_image = f"{Git}Desktop.png",
            large_text = f"{SysName}.",
            small_image = f"{Git}Info.png",
            small_text = f"{PyVer}.",
            name = f"{SysInfo}.",
            details = f"{DualVer}.",
            state =  f"Cpu: {cpu} | Ram: {mem}",
            start = int(start_time),
            buttons=[{"label": f"Check out Pypresence", "url": f"{PyPi}pypresence/"},
                    {"label": f"Check out Psutil", "url": f"{PyPi}psutil/"}]
        )

    time.sleep(5)