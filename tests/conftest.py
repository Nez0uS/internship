# tests/conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base
from models import Task


# Создаём тестовую БД в памяти (быстро, изолированно)
@pytest.fixture(scope="function")
def test_db():
    """Фикстура: создаёт чистую БД для каждого теста"""
    # 1. Движок для тестовой БД (SQLite в памяти)
    engine = create_engine("sqlite:///:memory:", echo=False)

    # 2. Создаём таблицы
    Base.metadata.create_all(engine)

    # 3. Сессия для работы
    TestingSessionLocal = sessionmaker(bind=engine)
    session = TestingSessionLocal()

    # 4. Возвращаем сессию в тест
    yield session

    # 5. Очищаем после теста (гарантированно, даже если тест упал)
    session.close()
    Base.metadata.drop_all(engine)


@pytest.fixture
def sample_task(test_db):
    """Фикстура: готовая задача для тестов"""
    task = Task(title="Тестовая задача", description="Для проверки")
    test_db.add(task)
    test_db.commit()
    test_db.refresh(task)  # Чтобы получить id после commit
    return task