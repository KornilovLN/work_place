#!/bin/bash

# Определение переменных
BASE_DIR="/home/$USER/work/docker"
PROJECT_DIR="$BASE_DIR/folder_site"
SERVER_PORT=8083
SERVER_URL="http://localhost:$SERVER_PORT"
FILE_MANAGER="Thunar"


# Переходим в рабочую директорию
cd $PROJECT_DIR

# Запускаем VSCode
code . &

# Открываем новый терминал Xfce4 и переходим в нужную папку
xfce4-terminal --working-directory="$PROJECT_DIR" &

# Открываем файловый менеджер в указанной папке
$FILE_MANAGER "$PROJECT_DIR" &

# Ждем немного, чтобы все процессы успели запуститься
sleep 2

# Выводим сообщение о завершении
echo "Все приложения запущены. Рабочее окружение готово."
