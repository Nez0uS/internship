from crud import create_task, get_all_tasks, get_task_by_id, update_task, delete_task


def test_create_task(test_db, monkeypatch):
    """Тест: создание задачи"""
    # Подменяем глобальную сессию в crud на тестовую
    monkeypatch.setattr("crud.session", test_db)

    # Act: выполняем действие
    task = create_task("Купить молоко", "2 литра")

    # Assert: проверяем результат
    assert task.id is not None
    assert task.title == "Купить молоко"
    assert task.description == "2 литра"
    assert task.completed == False


def test_get_all_tasks(test_db, monkeypatch):
    """Тест: получение всех задач"""
    monkeypatch.setattr("crud.session", test_db)

    # Создаём 3 задачи
    create_task("Задача 1")
    create_task("Задача 2")
    create_task("Задача 3")

    tasks = get_all_tasks()

    assert len(tasks) == 3
    assert all(isinstance(t, type(create_task("temp"))) for t in tasks)


def test_get_task_by_id_found(test_db, monkeypatch, sample_task):
    """Тест: поиск задачи по ID (успех)"""
    monkeypatch.setattr("crud.session", test_db)

    found = get_task_by_id(sample_task.id)

    assert found is not None
    assert found.id == sample_task.id
    assert found.title == "Тестовая задача"


def test_get_task_by_id_not_found(test_db, monkeypatch):
    """Тест: поиск задачи по ID (не найдено)"""
    monkeypatch.setattr("crud.session", test_db)

    found = get_task_by_id(999)  # Несуществующий ID

    assert found is None


def test_update_task(test_db, monkeypatch, sample_task):
    """Тест: обновление задачи"""
    monkeypatch.setattr("crud.session", test_db)

    result = update_task(sample_task.id, completed=True, title="Новое название")

    assert result == True
    updated = get_task_by_id(sample_task.id)
    assert updated.completed == True
    assert updated.title == "Новое название"


def test_delete_task(test_db, monkeypatch, sample_task):
    """Тест: удаление задачи"""
    monkeypatch.setattr("crud.session", test_db)

    result = delete_task(sample_task.id)

    assert result == True
    assert get_task_by_id(sample_task.id) is None


def test_delete_nonexistent_task(test_db, monkeypatch):
    """Тест: удаление несуществующей задачи"""
    monkeypatch.setattr("crud.session", test_db)

    result = delete_task(999)

    assert result == False

# def test_get_xfail(test_db, monkeypatch):
#     """Тест: должен вывести false и показать ошибку"""
#     monkeypatch.setattr("crud.session", test_db)
#
#     task = create_task("Погулять с собакой", "В 12:00")
#
#     assert delete_task(999) == True
#     assert task.id is None
#     assert task.title is None
# Я закомментировал, чтобы проверить, работают ли тесты правильно