# Python Project Management CLI Tool

A command-line application for managing users, projects, and tasks with persistent storage and a clean CLI interface.

---

## Features

- User management (add, list, delete users)
- Project management per user
- Task management inside projects
- Task tracking with priority and completion status
- Persistent data storage using JSON
- Clean CLI interface using argparse
- Rich terminal output formatting
- Automated testing with pytest

---

## Running Tests
pytest -v

### Architecture 

models/ → Defines User, Project, Task classes
services/ → Core logic + persistence layer
utils/ → CLI display formatting (Rich tables)
tests/ → Automated pytest test suite

## Author
John kingoo
