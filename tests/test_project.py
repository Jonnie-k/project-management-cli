from services.manager import ProjectManager

def test_add_project():
    pm = ProjectManager()

    pm.add_user("John", "john@example.com")
    pm.add_project("John", "Test Project")

    user = next(u for u in pm.list_users() if u.name == "John")

    assert any(p.title == "Test Project" for p in user.projects)