from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime

@dataclass
class Task:
    """Represents a single task in the task manager.

    Attributes:
        title: Task description.
        category: Optional grouping label.
        id: Unique identifier generated automatically.
        created_at: Timestamp of task creation.
        completed: Whether the task is done.
    """
    title: str
    category: str = ""
    id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(default_factory=datetime.now)
    completed: bool = False
