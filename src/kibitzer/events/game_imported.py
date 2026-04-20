from datetime import UTC, datetime
from typing import Literal
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


def _utc_now() -> datetime:
    return datetime.now(tz=UTC)


class GameImported(BaseModel):
    game_id: str
    played_at: datetime
    pgn: str
    white: str
    black: str
    result: Literal["1-0", "0-1", "1/2-1/2"]
    time_control: str
    event_id: UUID = Field(default_factory=uuid4)
    event_timestamp: datetime = Field(default_factory=_utc_now)
