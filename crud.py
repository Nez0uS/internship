from database import session
from models import Task


def create_task(title: str, description: str = "") -> Task:
    """Создаёт новую задачу"""
    task = Task(title=title, description=description)
    session.add(task)
    session.commit()
    return task


def get_all_tasks() -> list[Task]:
    """Возвращает все задачи"""
    tasks = session.query(Task).all()
    return tasks


def get_task_by_id(task_id: int) -> Task | None:
    """Ищет задачу по ID"""
    task = session.query(Task).filter(Task.id == task_id).first()
    return task


def update_task(task_id: int, **kwargs) -> bool:
    """Обновляет поля задачи. Возвращает True, если найдено"""
    task = session.query(Task).filter(Task.id == task_id).first()
    if task is None:
        return False

    for key, value in kwargs.items():
        setattr(task, key, value)

    session.commit()
    return True


def delete_task(task_id: int) -> bool:
    """Удаляет задачу. Возвращает True, если найдено"""
    task = session.query(Task).filter(Task.id == task_id).first()
    if task is None:
        return False
    session.delete(task)
    session.commit()
    return True
