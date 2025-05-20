import random
import datetime


class DateBegin:
    date_list = []

    def __init__(self, start_date, ad_count):
        """
        Конструктор класса DateBegin.

        Args:
            start_date (str): Дата начала расписания в формате "ДД.ММ.ГГГГ".
            ad_count (int): Общее количество объявлений, которые нужно опубликовать.
        """
        self.date_list = []
        start_date_dt = datetime.datetime.strptime(start_date, "%d.%m.%Y").date()

        current_date = start_date_dt
        while len(self.date_list) < ad_count:
            for hour in range(8, 24):  # с 8:00 до 23:00 включительно
                if len(self.date_list) >= ad_count:
                    break  # Прерываем цикл, если достигли ad_count

                minute = random.randint(0, 59)

                # Формируем datetime объект
                dt_object = datetime.datetime(current_date.year, current_date.month, current_date.day, hour, minute)

                # Форматируем в строку нужного формата
                date_string = dt_object.strftime("%d.%m.%y %H:%M")
                self.date_list.append(date_string)

            # Переходим к следующему дню
            current_date += datetime.timedelta(days=1)

    def get_random(self):
        """
        Получить случайную дату из списка.
        :return: str
        """
        return random.choice(self.date_list)


if __name__ == '__main__':
    # Пример использования
    start_date = "27.10.2023"
    ad_count = 55

    date_generator = DateBegin(start_date, ad_count)

    print(f"Сгенерировано {len(date_generator.date_list)} дат.")

    # Выводим несколько случайных дат для проверки
    for _ in range(5):
        print(date_generator.get_random())
