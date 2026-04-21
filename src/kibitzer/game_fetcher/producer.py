from confluent_kafka import Producer

from kibitzer.events.game_imported import GameImported

TOPIC = "games.imported"


class GameImportedProducer:
    def __init__(self, producer: Producer) -> None:
        self._producer = producer

    def publish(self, event: GameImported) -> None:
        self._producer.produce(
            topic=TOPIC,
            key=event.game_id.encode("utf-8"),
            value=event.model_dump_json().encode("utf-8"),
        )

    def flush(self) -> None:
        self._producer.flush()
