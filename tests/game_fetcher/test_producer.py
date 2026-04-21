from datetime import UTC, datetime
from unittest.mock import Mock

from confluent_kafka import Producer

from kibitzer.events.game_imported import GameImported
from kibitzer.game_fetcher.producer import GameImportedProducer


def _make_event() -> GameImported:
    return GameImported(
        game_id="abc123",
        played_at=datetime(2026, 4, 21, 11, 16, tzinfo=UTC),
        pgn="1. e4 e5 *",
        white="alice",
        black="bob",
        result="1-0",
        time_control="600",
    )


def test_publish_produces_to_games_imported() -> None:
    kafka_producer = Mock(spec=Producer)
    producer = GameImportedProducer(producer=kafka_producer)

    producer.publish(_make_event())
    kafka_producer.produce.assert_called_once()
    _, kwargs = kafka_producer.produce.call_args
    assert kwargs["topic"] == "games.imported"


def test_publish_uses_game_id_as_key() -> None:
    kafka_producer = Mock(spec=Producer)
    producer = GameImportedProducer(producer=kafka_producer)

    producer.publish(_make_event())

    _, kwargs = kafka_producer.produce.call_args
    assert kwargs["key"] == b"abc123"


def test_publish_serialises_event_as_json_bytes() -> None:
    kafka_producer = Mock(spec=Producer)
    producer = GameImportedProducer(producer=kafka_producer)

    event = _make_event()
    producer.publish(event)

    _, kwargs = kafka_producer.produce.call_args
    restored = GameImported.model_validate_json(kwargs["value"].decode("utf-8"))
    assert restored == event


def test_flush_delegates_to_underlying_producer() -> None:
    kafka_producer = Mock(spec=Producer)
    producer = GameImportedProducer(producer=kafka_producer)

    producer.flush()

    kafka_producer.flush.assert_called_once()
