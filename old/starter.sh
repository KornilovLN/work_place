#!/bin/bash

# Константа для пути к скриптам
SCRIPTS_DIR="scripts"

# Имена ваших трех скриптов
SCRIPT1="docker_spd-project_8082.sh"
SCRIPT2="sunpp_python_8083.sh"
SCRIPT3="sunpp_npx_8086.sh"

# Функция для проверки наличия скрипта
check_script() {
    if [ -f "$SCRIPTS_DIR/$1" ]; then
        echo "Скрипт $1 найден."
        return 0
    else
        echo "Скрипт $1 не найден."
        return 1
    fi
}

# Проверяем наличие всех скриптов
echo "Проверка наличия скриптов:"
check_script "$SCRIPT1"
check_script "$SCRIPT2"
check_script "$SCRIPT3"

# Запрашиваем у пользователя, какой скрипт запустить
echo -e "\nКакой скрипт вы хотите запустить?"
echo "1) $SCRIPT1"
echo "2) $SCRIPT2"
echo "3) $SCRIPT3"
read -p "Введите номер (1-3): " choice

# Выбираем скрипт на основе пользовательского ввода
case $choice in
    1) selected_script="$SCRIPT1" ;;
    2) selected_script="$SCRIPT2" ;;
    3) selected_script="$SCRIPT3" ;;
    *) echo "Неверный выбор. Пожалуйста, введите число от 1 до 3."; exit 1 ;;
esac

# Проверяем наличие выбранного скрипта перед запуском
if check_script "$selected_script"; then
    echo "Запускаем $selected_script"
    bash "$SCRIPTS_DIR/$selected_script"
else
    echo "Ошибка: Выбранный скрипт не найден. Выполнение прервано."
    exit 1
fi

