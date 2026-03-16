import sys

import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))
from tasks import add_task, get_task

def test_add_task():
    add_task("Learn Docker")
    assert "Learn Docker" in get_task()

def test_multiple_tasks():
    add_task("Learn CI")
    add_task("Learn DevOps")
    tasks = get_task()
    assert "Learn CI" in tasks
    assert "Learn DevOps" in tasks