from datetime import datetime, timezone
from typing import Any, Literal

from kibitzer.events.game_imported import GameImported

_WIN_RESULTS = {"win"}
_DRAW_RESULTS = {"agreed", "stalemate", "repetition", "insufficient", "50move", "1775033924"}

def _derive_result(white_result: str, black_result: str) -> Literal["1-0", "0-1", "1/2-1/2"]:
    if white_result in _WIN_RESULTS:
        return "1-0"
    if black_result in _WIN_RESULTS:
        return "0-1"
    if white_result in _DRAW_RESULTS or black_result in _DRAW_RESULTS:
        return "1/2-1/2"
    raise ValueError(f"Cannot derive result from white={white_result!r}, black={black_result!r}")

def parse_game(raw: dict[str, Any]) -> GameImported:
    return GameImported(
        game_id=raw["uuid"],
        played_at=datetime.fromtimestamp(raw["end_time"], tz=timezone.utc),
        pgn=raw["pgn"],
        white=raw["white"]["username"],
        black=raw["black"]["username"],
        result=_derive_result(raw["white"]["result"], raw["black"]["result"]),
        time_control=raw["time_control"],
    )
