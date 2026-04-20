import json
from pathlib import Path
from datetime import datetime, timezone

from kibitzer.game_fetcher.parser import parse_game
def test_parse_game_extracts_fields() -> None:
    raw = json.loads(
        (Path(__file__).parent.parent / "fixtures" / "sample_game.json").read_text()
    )
    event = parse_game(raw)

    assert event.game_id == "82d9e6da-2da8-11f1-8aee-1921a101000f"
    assert event.played_at == datetime.fromtimestamp(1775033924, tz=timezone.utc)
    assert event.white == "arunraghunath"
    assert event.black == "Ankeat"
    assert event.result == "0-1"
    assert event.time_control == "180"
    assert event.pgn.startswith("[Event \"Live Chess\"]")
