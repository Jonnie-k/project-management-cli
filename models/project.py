from models.task import Task


class Project:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_task(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                return task
        return None

    def remove_task(self, task_title):
        self.tasks = [
            task for task in self.tasks
            if task.title != task_title
        ]

    def completion_percentage(self):
        if not self.tasks:
            return 0

        completed = sum(
            1 for task in self.tasks if task.completed
        )

        return round(
            (completed / len(self.tasks)) * 100,
            2
        )

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "tasks": [
                task.to_dict()
                for task in self.tasks
            ]
        }

    @classmethod
    def from_dict(cls, data):
        project = cls(
            data["title"],
            data.get("description", "")
        )

        project.tasks = [
            Task.from_dict(task)
            for task in data.get("tasks", [])
        ]

        return project

    def __str__(self):
        return self.title