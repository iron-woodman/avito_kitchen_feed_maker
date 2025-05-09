@echo off
python "c:\avito_kitchen_feed_maker\main.py"
pause

@echo off

echo Запуск первого скрипта (создание ссылок на фото)...


python make_proper_urls.py

echo Первый скрипт завершен.

echo Запуск второго скрипта (создание фида автозагрузки)...
python main.py

echo Второй скрипт завершен.

pause
