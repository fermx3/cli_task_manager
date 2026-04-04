from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime

@dataclass
class Task:
    title: str
    category: str = ""
    id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(default_factory=datetime.now)
    completed: bool = False
