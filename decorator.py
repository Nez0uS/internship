import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)  # Вызываем функцию и сохраняем результат
        end = time.perf_counter()
        print(f"Время выполнения: {end - start:.6f} сек")
        return result  # Возвращаем результат работы функции
    return wrapper


@timing_decorator
def slow_function():
    time.sleep(2)


slow_function()
# 1 task is complate
# add commentary fot new branch on github
