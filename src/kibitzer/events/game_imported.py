from datetime import datetime
from typing import Literal

from kibitzer.events import BaseEvent


class GameImported(BaseEvent):
    game_id: str
    played_at: datetime
    pgn: str
    white: str
    black: str
    result: Literal["1-0", "0-1", "1/2-1/2"]
    time_control: str
