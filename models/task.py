from datetime import datetime


class Task:
    def __init__(
        self,
        title,
        description="",
        due_date=None,
        priority="Medium",
        completed=False
    ):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = completed

    def mark_complete(self):
        self.completed = True

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "priority": self.priority,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            description=data.get("description", ""),
            due_date=data.get("due_date"),
            priority=data.get("priority", "Medium"),
            completed=data.get("completed", False)
        )

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{self.title} [{status}]"