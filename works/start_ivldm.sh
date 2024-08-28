#!/bin/bash

# Определение переменных
PROJECT="ivldm"
WORKPLACE="/mnt/poligon"

BASE_DIR="/$WORKPLACE"
PROJECT_DIR="$BASE_DIR/$PROJECT"

FILE_MANAGER="Thunar"


# Переходим в рабочую директорию
cd $PROJECT_DIR

# Запускаем VSCode
code . &

# Открываем новый терминал Xfce4 и переходим в нужную папку
xfce4-terminal --working-directory=$PROJECT_DIR &

# Открываем файловый менеджер в указанной папке
xdg-open $PROJECT_DIR &

# Ждем немного, чтобы все процессы успели запуститься
sleep 2

# Выводим сообщение о завершении
echo "Все приложения в $PROJECT запущены. Рабочее окружение готово."
