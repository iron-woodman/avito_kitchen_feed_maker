import os
import shutil
import random

def distribute_photos(root_dir):
    """
    Обрабатывает каталог с фотографиями (*.jpeg) из каталога 'all',
    создает десять каталогов (1-10), раскидывает фото по этим каталогам
    в равной пропорции, переименовывает фото по шаблону: {номер каталога}_{порядковый номер фото в каталоге}.jpg,
    удаляет остаток фото из каталога 'all',
    а также удаляет исходные фото из каталога 'all' после распределения.
    """

    all_dir = os.path.join(root_dir, "all")
    output_dirs = [os.path.join(root_dir, str(i)) for i in range(1, 11)]

    # 0. Создание выходных каталогов, если они не существуют
    for output_dir in output_dirs:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"Создан каталог: {output_dir}")

    # 1. Сбор списка фотографий из каталога 'all'
    photos = [f for f in os.listdir(all_dir) if f.lower().endswith(".jpg")]
    random.shuffle(photos)  # Перемешиваем, чтобы распределение было более случайным

    num_photos = len(photos)
    photos_per_dir = num_photos // 10  # Целочисленное деление для определения количества фото на каталог
    remainder = num_photos % 10  # Определяем остаток

    # 2. Распределение фотографий по каталогам
    start_index = 0
    for i, output_dir in enumerate(output_dirs):
        dir_number = i + 1  # Номер текущего каталога (1-10)

        # Добавляем остаток к первым нескольким каталогам
        num_to_move = photos_per_dir + (1 if i < remainder else 0)

        end_index = start_index + num_to_move
        photos_to_move = photos[start_index:end_index]

        for j, photo in enumerate(photos_to_move):  # Добавляем порядковый номер
            source_path = os.path.join(all_dir, photo)
            new_filename = f"{dir_number}_{j + 1}.jpg"  # Формируем новое имя файла
            dest_path = os.path.join(output_dir, new_filename)
            shutil.move(source_path, dest_path)  # Перемещаем и переименовываем файлы

        start_index = end_index

    # 3. Удаление оставшихся фотографий из 'all' (теперь это должно быть пусто, но на всякий случай)
    for f in os.listdir(all_dir):
        file_path = os.path.join(all_dir, f)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)  # Удаляем файлы
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path) # Удаляем подкаталоги (если есть)
        except Exception as e:
            print(f"Не удалось удалить {file_path}. Ошибка: {e}")

    print("Фотографии успешно распределены, переименованы и остатки удалены!")

# Пример использования:
root_directory = r"F:\kwork\python\!avito_youla\avito_kitchen_feed_maker\company\kitchen\IMG\kitchen"  # Укажите корневой каталог, где находится 'all'
distribute_photos(root_directory)
