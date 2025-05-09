@echo off

echo Установка пакетов из requirements.txt...

REM Активируем виртуальное окружение (если оно используется)
if exist .\.venv\Scripts\activate.bat (
    call .\.venv\Scripts\activate.bat
) else (
    echo Виртуальное окружение не найдено.
)

REM Обновляем pip (рекомендуется)
echo Обновление pip...
python -m pip install --upgrade pip

REM Устанавливаем пакеты из requirements.txt
echo Установка пакетов...
python -m pip install -r requirements.txt

echo Установка пакетов завершена.
pause
