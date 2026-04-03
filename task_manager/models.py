from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime

@dataclass
class Task:
    id: UUID = field(default_factory=uuid4)
    title: str
    created_at: datetime = field(default_factory=datetime.now)
    category: str
    completed: bool = field(default=False)
