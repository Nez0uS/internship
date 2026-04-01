from crud import create_task, update_task, delete_task, get_all_tasks


def show_menu():
    print("\n" + "="*40)
    print("📋 Менеджер задач")
    print("="*40)
    print("1. Показать все задачи")
    print("2. Добавить задачу")
    print("3. Отметить задачу как выполненную")
    print("4. Удалить задачу")
    print("0. Выход")
    print("="*40)


def main() -> None:
    while True:
        show_menu()
        answer = input('Выберите действие: ')
        if answer == '1':
            tasks = get_all_tasks()
            if not tasks:
                print('Задач пока нет\n')
            else:
                for task in tasks:
                    print(f'{task.id}: {task.title}, {task.completed}')

        elif answer == '2':
            title_task_for_create = input('Задание: ')
            description_task_for_creat = input('Описание: ')
            if not title_task_for_create.strip():
                print('Название задания не может быть пустым\n')
                continue
            task_for_create = create_task(title_task_for_create, description_task_for_creat)
            print(task_for_create)

        elif answer == '3':
            try:
                id_task_change = int(input('Введите ID задания, которое выполнили: '))
                if update_task(id_task_change, completed=True):
                    print('Задача отмечена как выполненная\n')
                else:
                    print('Задачи с таким ID нет\n')
            except ValueError:
                print('Введите корректный номер ID\n')

        elif answer == '4':
            try:
                tasks = get_all_tasks()
                if not tasks:
                    print('Задач нету\n')
                    continue

                print('Ваши задачи:\n')
                for task in tasks:
                    print(f'{task.id}: {task.title}')
                id_task_for_delete = int(input('Введите ID задания для удаления: '))
                if delete_task(id_task_for_delete):
                    print('Задача удалена\n')
                else:
                    print('Задача с таким ID не найдена\n')
            except ValueError:
                print('Введите корректный номер\n')

        elif answer == '0':
            print('Выход...\n')
            break

        else:
            print('Выберите число от 0 до 4\n')

if __name__ == '__main__':
    main()