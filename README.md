# avito_kitchen_feed_maker

**Описание:**

Этот проект представляет собой скрипт на Python, предназначенный для автоматического создания XML-фида для автозагрузки объявлений на AVITO в категории "Кухонные гарнитуры". Он автоматизирует процесс подготовки данных о кухонных гарнитурах для публикации на платформе Avito.

## Установка и Настройка (Windows)

Следуйте этим инструкциям для установки и настройки проекта в системе Windows:

1.  **Распаковка проекта:**
    •   Извлеките содержимое архива проекта на диск `C:\` в каталог `avito_kitchen_feed_maker` (`C:\avito_kitchen_feed_maker`).
    •   **Внимание:** Вы можете выбрать другое место для распаковки проекта, но в этом случае необходимо будет обновить путь в файле `start.bat` в соответствии с выбранным местоположением.

2.  **Установка зависимостей:**
    •   В каталоге с проектом (`C:\avito_kitchen_feed_maker`) найдите и запустите файл `setup_on_windows.bat`.
    •   Этот файл установит все необходимые пакеты Python, требуемые для работы скрипта, с использованием менеджера пакетов `pip`.  Убедитесь, что `pip` установлен и доступен в вашей системе.

3.  **Настройка контента:**
    •   Перейдите в каталог `C:\avito_kitchen_feed_maker\company\kitchen\`.
    •   Здесь вы найдете файлы, которые необходимо настроить: тексты объявлений, заголовки и фотографии.  Внимательно отредактируйте эти файлы, чтобы отразить информацию о ваших кухонных гарнитурах.  Инструкции по формату и содержанию этих файлов должны быть указаны в документации к скрипту (или в комментариях в самих файлах).

4.  **Запуск скрипта:**
    •   Запустите файл `start.bat`, расположенный в корневом каталоге проекта (`C:\avito_kitchen_feed_maker`).
    •   Если все настройки выполнены правильно, скрипт создаст новый XML-файл фида с текущей датой в имени файла. Этот файл будет находиться в каталоге `C:\avito_kitchen_feed_maker\company\kitchen\feeds\`.

5.  **Загрузка изображений:**
    •   Загрузите фотографии кухонных гарнитуров на хостинг изображений, URL которого указан в настройках скрипта (либо в файлах конфигурации, которые вы редактировали на шаге 3).  Важно, чтобы все фотографии были доступны по указанным URL.

6.  **Проверка URL изображений:**
    •   Убедитесь, что все ссылки на фотографии в созданном XML-фиде ведут на корректные изображения, которые открываются в браузере.

7.  **Проверка фида на валидность:**
    •   Перейдите на страницу проверки XML-фида AVITO: [https://autoload.avito.ru/format/xmlcheck/](https://autoload.avito.ru/format/xmlcheck/)
    •   Загрузите созданный XML-файл фида и проверьте его на соответствие требованиям AVITO.  Исправьте любые ошибки, обнаруженные в процессе проверки.

8.  **Загрузка фида на AVITO:**
    •   После успешного прохождения всех проверок вы можете загрузить XML-файл фида на сайт AVITO.RU для автоматической публикации объявлений о кухонных гарнитурах.

**Важно:**

•   Перед запуском скрипта убедитесь, что все необходимые настройки выполнены правильно, особенно пути к файлам и настройки хостинга изображений.
•   Регулярно проверяйте XML-фид на соответствие требованиям AVITO, так как требования могут меняться.
•   Внимательно изучите документацию к скрипту для получения более подробной информации о настройке и использовании.
