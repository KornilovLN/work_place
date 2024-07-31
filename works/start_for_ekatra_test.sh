#!/bin/bash

WORK_PATH="/mnt/poligon/for_ekatra_test"

# Переходим в рабочую директорию
cd $WORK_PATH

# Запускаем VSCode
code . 

# Открываем новый терминал Xfce4 и переходим в нужную папку
xfce4-terminal --working-directory=$WORK_PATH

# Открываем файловый менеджер в указанной папке
xdg-open $WORK_PATH
