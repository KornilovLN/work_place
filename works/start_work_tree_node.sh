#!/bin/bash

# Переходим в рабочую директорию
cd ~/work/docker/tree_node

# Запускаем VSCode
code . 

# Открываем новый терминал Xfce4 и переходим в нужную папку
xfce4-terminal --working-directory="~/work/docker/tree_node"

# Открываем файловый менеджер в указанной папке
xdg-open ~/work/docker/tree_node
