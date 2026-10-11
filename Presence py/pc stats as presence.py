from pypresence import Presence
from pypresence.types import ActivityType, StatusDisplayType
import pypresence
import time
from time import sleep
import psutil
import platform
import os
import socket
import pystray
from PIL import Image, ImageDraw
import os
import threading

#code
Git = "https://raw.githubusercontent.com/ArchitectureX86/Discord-Rich-Presence/refs/heads/main"
GitAss = f"{Git}/Presence%20py/assets"
PyPi = "https://pypi.org/project"
SysPr = platform.release()
SysInfo = f"{platform.system()} {SysPr} {os.name}"
SysName = f"{socket.gethostname()}"
SysUser = os.environ.get("USERNAME", "Unknown user")
PyVer = f"🐍v{platform.python_version()}"
PypVer = f"PyPresence v{pypresence.__version__}"
PsuVer = f"Psutil v{psutil.__version__}"
DualVer = f"{PypVer} | {PsuVer}"

print("God oh fucking help me ouch it burns augh my dick pleaseeee")

client_id = "1546844285645627542"
RPC = Presence(client_id)
def tryconnect():
    active = 0
    while active == 0:
        try:
            RPC.connect()
            active = 1
        except:
            sleep(5)

tryconnect()

start_time = (time.time())

def regular_stuff():
    while True:
        cpu = f"{int(psutil.cpu_percent(interval=None))}%"
        mem = f"{int(psutil.virtual_memory().percent)}%"
    # Show as "Playing"
        try:
            RPC.update(
                    large_image = f"{GitAss}/Desktop/{SysPr}.png",
                    large_text = f"{SysName}.",
                    small_image = f"{GitAss}/Info/{SysPr}i.png",
                    small_text = f"{PyVer}.",
                    name = f"{SysInfo}.",
                    details = f"{DualVer}.",
                    state =  f"Cpu: {cpu} | Ram: {mem}",
                    start = int(start_time),
                    buttons=[{"label": f"This presence on github:", "url": f"{Git}"},
                            {"label": f"Check out Pypresence", "url": f"{PyPi}/pypresence"}]
                )
        except:
            time.sleep(1)

        time.sleep(5)

# tray
def create_image():
    # Generates a simple colored square as a placeholder tray icon
    image = Image.new('RGB', (64, 64), color=(73, 109, 137))
    dc = ImageDraw.Draw(image)
    dc.rectangle((16, 16, 48, 48), fill=(255, 255, 255))
    return image

def on_quit(icon, item):
    icon.stop()

if __name__ == "__main__":
    # Runs the tray loop in the background
    t = threading.Thread(target=regular_stuff, daemon=True)
    t.start()
    # Define the tray menu
    menu = pystray.Menu(pystray.MenuItem('Quit', on_quit))

    # Create the icon instance
    icon = pystray.Icon("background_process", create_image(), "My Stealthy App", menu)
    icon.run()