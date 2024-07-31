#!/bin/bash

# start_work_rabbitmq.sh

# Определение переменных
PROJECT="rabbitmq"
WORKPLACE="virt/dockers"

BASE_DIR="$HOME/$WORKPLACE"
PROJECT_DIR="$BASE_DIR/$PROJECT"

FILE_MANAGER="Thunar"

# Переходим в рабочую директорию
cd $PROJECT_DIR

# Запускаем VSCode
code . 

# Открываем новый терминал Xfce4 и переходим в нужную папку
xfce4-terminal --working-directory=$PROJECT_DIR

# Открываем файловый менеджер в указанной папке
xdg-open $PROJECT_DIR
