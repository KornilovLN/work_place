#!/bin/bash

#--- Запуск контейнера с SPD_new с привязкой к SERVER_POR на хосте
#--- работает локальный сервер (в этом случае из докер-контейнера)
#--- Браузер будет определен и запущен функцией open_browser() на хосте

SERVER_PORT=8082
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

# Запуск докера в фоновом или интерактивном режиме
docker run --rm  -d -p $SERVER_PORT:8080 spd-project
#docker run --rm -it -p $SERVER_PORT:8080 spd-project


# Ждем, пока сервер не запустится (вы должны увидеть соответствующее сообщение в терминале)
#read -p "Нажмите Enter, когда сервер будет готов..."
sleep 5


# Открываем браузер
open_browser 


#--- после закрытия контейнера на хосте порт будет освобожден
#--- Как остановить контейнер и удалить из памяти:
#  > docker ps [-a]                        <- покажет инфо о работающих контейнерах
#  > docker stop <текущее имя контейнера>  <- имя взять из этого инфо (в конце строки)
#  > docker start <текущее имя контейнера> <- но если надо - продолжить работать с контейнером
#  > docker rm <текущее имя контейнера>    <- или удалить из памяти остановленный контейнер
#--- теперь порт свободен и уже localhost:8082 отзываться не будет 











