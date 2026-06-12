from models.user import User
from models.project import Project
from models.task import Task

from services.storage import load_data, save_data
from services.logger import logger


class ProjectManager:

    def __init__(self):
        self.users = load_data() or []

    # ===================
    # STORAGE WRAPPERS
    # ===================

    def save_data(self):
        """
        Wrapper so tests and CLI can call pm.save_data()
        """
        save_data(self.users)

    def reload_data(self):
        """
        Optional helper (useful for testing)
        """
        self.users = load_data() or []

    # ===================
    # USERS
    # ===================

    def add_user(self, name, email=""):
        user = User(name, email)
        self.users.append(user)

        save_data(self.users)

        logger.info(f"Added user: {name}")

    def list_users(self):
        return self.users

    def get_user(self, name):
        return next((u for u in self.users if u.name == name), None)

    def delete_user(self, name):
        self.users = [u for u in self.users if u.name != name]
        save_data(self.users)

    # ===================
    # PROJECTS
    # ===================

    def add_project(self, username, title, description=""):
        user = self.get_user(username)

        if not user:
            raise ValueError("User not found")

        project = Project(title, description)
        user.add_project(project)

        save_data(self.users)

        logger.info(f"Project '{title}' added to {username}")

    def list_projects(self, username):
        user = self.get_user(username)
        return user.projects if user else []

    def get_project(self, username, project_title):
        user = self.get_user(username)
        return user.get_project(project_title) if user else None

    def delete_project(self, username, project_title):
        user = self.get_user(username)

        if user:
            user.remove_project(project_title)
            save_data(self.users)

    # ===================
    # TASKS
    # ===================

    def add_task(
        self,
        username,
        project_title,
        task_title,
        description="",
        due_date=None,
        priority="Medium"
    ):
        project = self.get_project(username, project_title)

        if not project:
            raise ValueError("Project not found")

        task = Task(task_title, description, due_date, priority)
        project.add_task(task)

        save_data(self.users)

        logger.info(f"Task '{task_title}' added to {project_title}")

    def list_tasks(self, username, project_title):
        project = self.get_project(username, project_title)
        return project.tasks if project else []

    def complete_task(self, username, project_title, task_title):
        project = self.get_project(username, project_title)

        if not project:
            raise ValueError("Project not found")

        task = project.get_task(task_title)

        if not task:
            raise ValueError("Task not found")

        task.mark_complete()

        save_data(self.users)

    # ===================
    # DASHBOARD
    # ===================

    def dashboard(self):
        total_users = len(self.users)

        total_projects = sum(len(u.projects) for u in self.users)

        total_tasks = sum(
            len(p.tasks)
            for u in self.users
            for p in u.projects
        )

        completed_tasks = sum(
            1
            for u in self.users
            for p in u.projects
            for t in p.tasks
            if t.completed
        )

        return {
            "users": total_users,
            "projects": total_projects,
            "tasks": total_tasks,
            "completed": completed_tasks
        }