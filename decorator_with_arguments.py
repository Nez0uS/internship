def retry(max_attempts):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(1, max_attempts+1):
                try:
                    result = func(*args, **kwargs)
                    print(f"Успешно с попытки {i}")
                    return result
                except Exception as e:
                    last_exception = e

                    if i < max_attempts:
                        print(f"Попытка {i}/{max_attempts}")

            raise last_exception
        return wrapper
    return decorator


@retry(max_attempts=3)
def unstable_function():
    import random
    if random.random() < 0.7:  # 70% шанс ошибки
        raise ValueError("Случайная ошибка!")
    return "Успех!"

unstable_function()