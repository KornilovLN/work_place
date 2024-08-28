#!/bin/bash

#--- Запуск контейнера с app.py доступа к таблице bg_db_star
#--- базы данных postgresql,  запущенной в контейнере на
#--- удаленной VM

IMAGENAME="app_to_postgres:latest"
CONTAINERNAME="app_postgres_cont"
PORTHOST=5000
PORTDOCK=5000
SERVER_URL="http://localhost:$PORTHOST"

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

# Запуск докера в фоновом или интерактивном режиме
# Если был запущен, то надо остановить перед перегрузкой 
docker stop $CONTAINERNAME

sleep 2

# Создаем том для контекста, создаваемого приложением
docker volume create $VOLUMENAME


# После останова самоуничтожится
docker run  --rm \
            --name $CONTAINERNAME \
            -p $PORTHOST:$PORTDOCK \
            $IMAGENAME


# Ждем, пока сервер не запустится 
sleep 10


# Открываем браузер
open_browser 
