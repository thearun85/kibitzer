from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from kibitzer.events.game_imported import GameImported


def test_game_imported_roundtrips_through_json() -> None:
    original = GameImported(
        game_id="abc123",
        played_at=datetime(2026, 4, 20, 20, 57, tzinfo=UTC),
        pgn="1. e4 e5 2. Nf3 Nc6 *",
        white="alice",
        black="bob",
        result="1-0",
        time_control="600",
    )

    json_str = original.model_dump_json()
    restored = GameImported.model_validate_json(json_str)

    assert restored == original


def test_game_imported_rejects_invalid_result() -> None:
    with pytest.raises(ValidationError):
        GameImported(
            game_id="abc123",
            played_at=datetime(2026, 4, 20, 21, 14, tzinfo=UTC),
            pgn="1. e4 *",
            white="alice",
            black="Bob",
            result="win",  # type: ignore[arg-type]
            time_control="600",
        )


def test_game_imported_defaults_event_id_and_timestamp() -> None:
    before = datetime.now(tz=UTC)
    event = GameImported(
        game_id="abc123",
        played_at=datetime(2026, 4, 20, 21, 20, tzinfo=UTC),
        pgn="1. e4 e5 *",
        white="alice",
        black="bob",
        result="1-0",
        time_control="600",
    )

    after = datetime.now(tz=UTC)
    assert before <= event.event_timestamp <= after

    other = GameImported(
        game_id="abc123",
        played_at=datetime(2026, 4, 20, 21, 20, tzinfo=UTC),
        pgn="1. e4 e5 *",
        white="alice",
        black="bob",
        result="1-0",
        time_control="600",
    )
    assert event.event_id != other.event_id
