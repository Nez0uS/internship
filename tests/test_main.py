from main import show_menu  # Если вынесешь логику в отдельные функции

def test_show_menu_output(capsys):
    """Тест: проверка вывода меню"""
    show_menu()
    captured = capsys.readouterr()
    assert "📋 Менеджер задач" in captured.out
    assert "1. Показать все задачи" in captured.out