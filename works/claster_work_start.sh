#!/bin/bash

# Определение переменных
PROJECT="claster_spd"
WORKPLACE="/work/docker"

BASE_DIR="/home/$USER/$WORKPLACE"
PROJECT_DIR="$BASE_DIR/$PROJECT"

SERVER_PORT=8084
SERVER_URL="http://localhost:$SERVER_PORT"

FILE_MANAGER="Thunar"


# Переходим в рабочую директорию
cd $PROJECT_DIR

# Запускаем VSCode
code . &

# Открываем новый терминал Xfce4 и переходим в нужную папку
xfce4-terminal --working-directory="$PROJECT_DIR" &

# Открываем файловый менеджер в указанной папке
xdg-open ~/work/docker/claster_spd

# Ждем немного, чтобы все процессы успели запуститься
sleep 2

# Выводим сообщение о завершении
echo "Приложения запущены. Рабочее окружение $PROJECT готово."
