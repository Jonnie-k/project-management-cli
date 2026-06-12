from services.manager import ProjectManager

def test_add_user():
    pm = ProjectManager()
    initial_count = len(pm.list_users())

    pm.add_user("TestUser", "test@example.com")

    assert len(pm.list_users()) == initial_count + 1