import json
import os

from models.user import User

DATA_FILE = "data.json"


def load_data():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

        return [
            User.from_dict(user)
            for user in data
        ]

    except json.JSONDecodeError:
        return []


def save_data(users):
    with open(DATA_FILE, "w") as file:
        json.dump(
            [user.to_dict() for user in users],
            file,
            indent=4
        )