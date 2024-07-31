#!/usr/bin/env bash

# Определение переменных
PRJ_NAME="sunpp_docs"
BASE_DIR="/home/$USER/work/docker/folder_site"
PROJECT_DIR="$BASE_DIR/$PRJ_NAME"
SERVER_PORT=8086
SERVER_URL="http://localhost:$SERVER_PORT"
FILE_MANAGER="Thunar"

# Создаем команду для выполнения в новом терминале
COMMAND="cd '$PROJECT_DIR' && \
python3 -m http.server $SERVER_PORT & \
SERVER_PID=\$! && \
sleep 5 && \
xdg-open '$SERVER_URL' && \
xdg-open '$PROJECT_DIR' && \
echo 'Сервер с $PRJ_NAME запущен на $SERVER_URL' && \
echo 'Нажмите Enter для завершения работы сервера и закрытия всех окон...' && \
read && \
kill \$SERVER_PID && \
killall $FILE_MANAGER && \
echo 'Скрипт с работой над $PRJ_NAME завершен.' && \
echo 'Нажмите Enter, чтобы закрыть это окно...' && \
read"

# Запускаем новый терминал с нашей командой
xfce4-terminal --hold -e "bash -c \"$COMMAND\""

echo "Основной скрипт завершен. Новый терминал открыт для работы с $PRJ_NAME."

