from pypresence import Presence
from pypresence.types import ActivityType, StatusDisplayType
import pypresence
import pytest
import time
import psutil
import platform
import os
import socket

Git = "https://raw.githubusercontent.com/ArchitectureX86/Discord-Rich-Presence/refs/heads/main/Presence%20py/assets"
PyPi = "https://pypi.org/project/"
SysPr = platform.release()
SysInfo = f"{platform.system()} {SysPr} {os.name}"
SysName = f"{socket.gethostname()}"
SysUser = os.environ.get("USERNAME", "Unknown user")
PyVer = f"🐍v{platform.python_version()}"
PypVer = f"PyPresence v{pypresence.__version__}"
PsuVer = f"Psutil v{psutil.__version__}"
DualVer = f"{PypVer} | {PsuVer}"

client_id = "1546844285645627542"
RPC = Presence(client_id)
RPC.connect()

start_time = (time.time())

def test_example():
    while True:
        cpu = f"{int(psutil.cpu_percent(interval=None))}%"
        mem = f"{int(psutil.virtual_memory().percent)}%"
    # Show as "Playing"
        RPC.update(
                large_image = f"{Git}/Desktop/{SysPr}.png",
                large_text = f"{SysName}.",
                small_image = f"{Git}/Info/{SysPr}i.png",
                small_text = f"{PyVer}.",
                name = f"{SysInfo}.",
                details = f"{DualVer}.",
                state =  f"Cpu: {cpu} | Ram: {mem}",
                start = int(start_time),
                buttons=[{"label": f"This presence on github:", "url": f"https://github.com/ArchitectureX86/Discord-Rich-Presence"},
                        {"label": f"Check out Pypresence", "url": f"{PyPi}pypresence/"}]
            )

        time.sleep(5)