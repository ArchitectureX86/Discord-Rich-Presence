from pypresence import Presence
from pypresence.types import ActivityType, StatusDisplayType
import time
import datetime
import psutil
from pathlib import Path

client_id = "1546844285645627542"
RPC = Presence(client_id)
RPC.connect()

while True:
    Limage = 'https://avatars.githubusercontent.com/u/1965106'
    print("Getting cpu")
    cpu = f"{psutil.cpu_percent(interval=None)}%"
    print("Got cpu")

    print("Getting ram")
    mem = f"{psutil.virtual_memory().percent}%"
    print("Got ram")
# Show as "Playing"
    RPC.update(
            large_image="https://raw.githubusercontent.com/ArchitectureX86/new-website/refs/heads/main/images/ash_water.png",
            state=".",
            details=f"Cpu: {cpu} / Ram: {mem}",
            name=".",
        )
    print("des q-dos")

    time.sleep(5)
