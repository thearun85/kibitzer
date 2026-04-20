from datetime import UTC, datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


def _utc_now() -> datetime:
    return datetime.now(tz=UTC)


class BaseEvent(BaseModel):
    event_id: UUID = Field(default_factory=uuid4)
    event_timestamp: datetime = Field(default_factory=_utc_now)
