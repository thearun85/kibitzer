from datetime import UTC, datetime

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
