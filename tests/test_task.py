from services.manager import ProjectManager

def test_add_task():
    pm = ProjectManager()

    pm.add_user("John", "john@example.com")
    pm.add_project("John", "Website")
    pm.add_task("John", "Website", "Build Homepage")

    user = next(u for u in pm.list_users() if u.name == "John")
    project = next(p for p in user.projects if p.title == "Website")

    assert any(t.title == "Build Homepage" for t in project.tasks)