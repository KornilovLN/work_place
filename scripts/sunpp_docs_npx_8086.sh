#!/usr/bin/env bash

#--- Запуск сервера (можно питоновский локальный сервер) с SERVER_PORT
#--- на localhost. Выбрали порт 8086
#--- Также запустили файловый менеджер (Thunar)
#--- и организуем выход из работы с остановкой и удалением сервера

# Определение переменных
PRJ_NAME="sunpp_docs"
BASE_DIR="/home/$USER/work/docker/folder_site"
PROJECT_DIR="$BASE_DIR/$PRJ_NAME"
SERVER_PORT=8086
SERVER_URL="http://localhost:$SERVER_PORT"
FILE_MANAGER="Thunar"


# Функция для открытия браузера
open_browser() {
    if command -v xdg-open &> /dev/null; then
        xdg-open "$SERVER_URL"
    elif command -v gnome-open &> /dev/null; then
        gnome-open "$SERVER_URL"
    elif command -v open &> /dev/null; then
        open "$SERVER_URL"
    else
        echo "Не удалось автоматически открыть браузер. Пожалуйста, откройте $SERVER_URL вручную."
    fi
}

# Переходим в рабочую директорию
cd "$PROJECT_DIR"

# Запускаем Python SimpleHTTPServer (питоновский локальный сервер)
python3 -m http.server $SERVER_PORT &
SERVER_PID=$!

# Ждем немного, чтобы сервер успел запуститься
sleep 5

# Открываем браузер
open_browser &

# Открываем файловый менеджер в указанной папке
xdg-open "$PROJECT_DIR" &

# Небольшая задержка перед открытием терминала
sleep 1


# Создаем временный скрипт для нового терминала
cat << EOF > temp_terminal_script.sh
#!/bin/bash
echo "Сервер с $PRJ_NAME запущен на $SERVER_URL"
echo "Нажмите Enter для завершения работы сервера и закрытия всех окон..."
read
kill $SERVER_PID
killall $FILE_MANAGER  # Замените на имя вашего файлового менеджера
exit
EOF

# Делаем его исполняемым
chmod +x temp_terminal_script.sh


# Открываем новый терминал Xfce4 с временным скриптом
xfce4-terminal --working-directory="$PROJECT_DIR" -e "./temp_terminal_script.sh"

# Ждем завершения работы временного скрипта
wait

# Удаляем временный скрипт
rm temp_terminal_script.sh

echo "Скрипт с работой над $PRJ_NAME завершен."
