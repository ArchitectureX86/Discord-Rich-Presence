from pypresence import Presence
from pypresence.types import ActivityType, StatusDisplayType
import time
import psutil

client_id = "1546844285645627542"
RPC = Presence(client_id)
RPC.connect()

# Show as "Playing"
RPC.update(
        state="Doin' cool stuff.",
        details="Making my own Rich Presence with pypresence!",
        name="Custom presence!",
    )

# I haven't looked at this yet, grapped from "https://qwertyquerty.github.io/pypresence/html/info/quickstart.html".
'''
# Make state and details clickable
RPC.update(
    state="Playing an Awesome Game",
    state_url="https://example.com/game",
    details="In the Main Menu",
    details_url="https://example.com/game/menu"
)

# Make images clickable
RPC.update(
    large_image="game_logo",
    large_text="My Game",
    large_url="https://example.com/game",
    small_image="status_online",
    small_text="Online",
    small_url="https://example.com/status"
)
'''

# Show as "Listening to",
# probably never using this.
'''
RPC.update(
    activity_type=ActivityType.LISTENING,
    details="Some weird song",
    state="By some guy"
)
'''

# StatusDisplayType to control the status..?
'''
RPC.update(
    status_display_type=StatusDisplayType.STATE,
    state="Bingo Bango Busboy",
    details="Using Pypresence"
)
'''

while True:
    time.sleep(15)
