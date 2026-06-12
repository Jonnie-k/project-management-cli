from services.manager import ProjectManager

def test_save_and_load():
    pm = ProjectManager()

    pm.add_user("PersistUser", "persist@test.com")
    pm.save_data()

    pm2 = ProjectManager()  # reload

    users = pm2.list_users()
    assert any(u.name == "PersistUser" for u in users)
    