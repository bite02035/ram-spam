import numpy as np
import time


def allocate_memory(mb):
    # Перевод в байты
    size_bytes = mb * 1024 * 1024
    # Выделение памяти
    data = np.random.rand(size_bytes // 8)  # создаем массив случайных чисел (8 байт на элемент для float64)
    # Про float32 колво занимаемой оператавы становится неуправляемым и улетает в космос

    try:
        # Чтобы не оффалось
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Программа завершена.")


if __name__ == "__main__":
    try:
        mb = int(input("Введите количество МБ для загрузки оперативной памяти: "))
        allocate_memory(mb)
    except ValueError:
        print("Пожалуйста, введите корректное число.")
