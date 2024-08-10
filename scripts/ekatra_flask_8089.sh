#!/bin/bash

#--- Запуск контейнера с ekatra_lask с привязкой к SERVER_PORT на хосте
#--- работает локальный сервер (в этом случае из докер-контейнера)
#--- Браузер будет определен и запущен функцией open_browser() на хосте

IMAGENAME="my-flask-img:latest"
CONTAINERNAME="my-flask-cont"
VOLUMENAME="ekatra_flask_data"
VOLUMEPATH="/home/leon/work/docker/ekatra_flask/"
APPPATH="/app"
DATAPATH="/data"
PORTHOST=8089
PORTDOCK=80
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
            -v $VOLUMEPATH:$APPPATH \
            -v $VOLUMENAME:$DATAPATH \
            $IMAGENAME


# Ждем, пока сервер не запустится 
sleep 10


# Открываем браузер
open_browser 






