from rich.console import Console
from rich.table import Table

console = Console()


def show_users(users):
    table = Table(title="Users")

    table.add_column("Name")
    table.add_column("Email")

    for user in users:
        table.add_row(user.name, user.email)

    console.print(table)


def show_projects(projects):
    table = Table(title="Projects")

    table.add_column("Title")
    table.add_column("Description")

    for project in projects:
        table.add_row(
            project.title,
            project.description
        )

    console.print(table)


def show_tasks(tasks):
    table = Table(title="Tasks")

    table.add_column("Task")
    table.add_column("Priority")
    table.add_column("Completed")

    for task in tasks:
        table.add_row(
            task.title,
            task.priority,
            str(task.completed)
        )

    console.print(table)


def show_dashboard(stats):
    table = Table(title="Dashboard")

    table.add_column("Metric")
    table.add_column("Value")

    for key, value in stats.items():
        table.add_row(
            key.capitalize(),
            str(value)
        )

    console.print(table)