#!/bin/bash

#--- Запуск контейнера с my-flask-cont с привязкой к SERVER_PORT
#--- удаленном сервере как localhost:$SERVER_PORT с хоста своего
#--- Запуск сначала подключения к удаленному серверу по SSH командой
#--- ssh -L 8089:localhost:8089 starmark@gitlab.ivl.ua 
#--- Что связывает доступ через 2 порта (свой и удаленный) 
#--- Удаленно работает локальный сервер
#--- (в этом случае из докер-контейнера),
#--- который там запущен для входа из браузера localhost:8089
#--- Браузер будет определен и запущен функцией open_browser() на хосте

SERVER_PORT=8089
SERVER_URL="http://localhost:$SERVER_PORT"

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

# подключение по SSH к удаленному серверу с пробросом портов
ssh -L 8089:localhost:8089 starmark@gitlab.ivl.ua 

sleep 5

# на сервере уже работает докер-контейнер с приложением сайта

# Открываем браузер
open_browser 









