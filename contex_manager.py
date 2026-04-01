import time


class TimerContext:
    def __init__(self, name: str):
        self.name = name

    def __enter__(self):
        self.start = time.perf_counter()
        return self  # Это попадёт в переменную после 'as'

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        print(f'{self.name} выполнена за {self.end - self.start:.6f} сек')
        # Если вернёт True - ошибка будет "проглочена"
        return False


with TimerContext("Моя операция"):
    time.sleep(1)

# Вроде сделал, работает =) Надеюсь правильно