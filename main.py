import datetime
from crud import *
from database import session
from models import Task

answer = input('''
1. Показать все задачи
2. Добавить задачу
3. Отметить задачу как выполненную
4. Удалить задачу
0. Выход

Ответ:
''')

if answer == '1':
    title_task_for_create = input('Задание: ')
    description_task_for_creat = input('Описание: ')
    task_for_create = create_task(title_task_for_create, description_task_for_creat)
    print(task_for_create)

elif answer == '2':
    print(get_all_tasks())

elif answer == '3':
    id_task_change = input('Введите ID задания, которое выполнили: ')
    task = get_task_by_id(id_task_change)
    task.completed = True
    print(task)

elif answer == '4':
    print(get_all_tasks())
    id_task_for_delete = input('Введите ID задания для удаления: ')
    delete_task(id_task_for_delete)

elif answer == '0':
    print('Выход...')
