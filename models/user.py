from models.project import Project


class User:
    def __init__(self, name, email=""):
        self.name = name
        self.email = email
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def get_project(self, project_title):
        for project in self.projects:
            if project.title == project_title:
                return project
        return None

    def remove_project(self, project_title):
        self.projects = [
            project for project in self.projects
            if project.title != project_title
        ]

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "projects": [
                project.to_dict()
                for project in self.projects
            ]
        }

    @classmethod
    def from_dict(cls, data):
        user = cls(
            data["name"],
            data.get("email", "")
        )

        user.projects = [
            Project.from_dict(project)
            for project in data.get("projects", [])
        ]

        return user

    def __str__(self):
        return self.name