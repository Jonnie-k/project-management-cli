import argparse

from services.manager import ProjectManager
from utils.display import (
    show_users,
    show_projects,
    show_tasks,
    show_dashboard
)


def main():
    pm = ProjectManager()

    parser = argparse.ArgumentParser(
        description="Project Management CLI Tool"
    )

    subparsers = parser.add_subparsers(
        dest="command"
    )

    # add-user
    add_user = subparsers.add_parser(
        "add-user"
    )
    add_user.add_argument(
        "--name",
        required=True
    )
    add_user.add_argument(
        "--email",
        default=""
    )

    # list-users
    subparsers.add_parser(
        "list-users"
    )

    # add-project
    add_project = subparsers.add_parser(
        "add-project"
    )

    add_project.add_argument(
        "--user",
        required=True
    )

    add_project.add_argument(
        "--title",
        required=True
    )

    add_project.add_argument(
        "--description",
        default=""
    )

    # list-projects
    list_projects = subparsers.add_parser(
        "list-projects"
    )

    list_projects.add_argument(
        "--user",
        required=True
    )

    # add-task
    add_task = subparsers.add_parser(
        "add-task"
    )

    add_task.add_argument(
        "--user",
        required=True
    )

    add_task.add_argument(
        "--project",
        required=True
    )

    add_task.add_argument(
        "--title",
        required=True
    )

    # list-tasks
    list_tasks = subparsers.add_parser(
        "list-tasks"
    )

    list_tasks.add_argument(
        "--user",
        required=True
    )

    list_tasks.add_argument(
        "--project",
        required=True
    )

    # complete-task
    complete = subparsers.add_parser(
        "complete-task"
    )

    complete.add_argument(
        "--user",
        required=True
    )

    complete.add_argument(
        "--project",
        required=True
    )

    complete.add_argument(
        "--title",
        required=True
    )

    # dashboard
    subparsers.add_parser(
        "dashboard"
    )

    args = parser.parse_args()

    try:

        if args.command == "add-user":
            pm.add_user(
                args.name,
                args.email
            )

            print("User added successfully")

        elif args.command == "list-users":
            show_users(
                pm.list_users()
            )

        elif args.command == "add-project":
            pm.add_project(
                args.user,
                args.title,
                args.description
            )

            print("Project added")

        elif args.command == "list-projects":
            show_projects(
                pm.list_projects(
                    args.user
                )
            )

        elif args.command == "add-task":
            pm.add_task(
                args.user,
                args.project,
                args.title
            )

            print("Task added")

        elif args.command == "list-tasks":
            show_tasks(
                pm.list_tasks(
                    args.user,
                    args.project
                )
            )

        elif args.command == "complete-task":
            pm.complete_task(
                args.user,
                args.project,
                args.title
            )

            print(
                "Task completed"
            )

        elif args.command == "dashboard":
            show_dashboard(
                pm.dashboard()
            )

        else:
            parser.print_help()

    except Exception as e:
        print(
            f"Error: {e}"
        )


if __name__ == "__main__":
    main()