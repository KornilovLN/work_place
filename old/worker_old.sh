#!/bin/bash

# Константа для пути к скриптам
SCRIPTS_DIR="works"

# Имена ваших трех скриптов
WORK1="start_work_tree_node.sh"
WORK2="start_work_folder_site.sh"

WORK3="start_comment_sunpp.sh"

WORK4="docker_simple_docs.sh"
WORK5="claster_work_start.sh"

WORK6="start_install_sunpp_2vm.sh"
WORK7="start_install_sunpp_2_vm-docker.sh"
WORK8="start_multi_dockers.sh"
WORK9="start_multi_vm_gen_db_view_repo.sh"

WORK10="start_for_ekatra_test.sh"

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

echo "Проверка наличия скриптов:"
check_script "$WORK1"
check_script "$WORK2"
check_script "$WORK3"
check_script "$WORK4"
check_script "$WORK5"
check_script "$WORK6"
check_script "$WORK7"
check_script "$WORK8"
check_script "$WORK9"
check_script "$WORK10"

echo -e "\nКакой скрипт вы хотите запустить?"
echo "1) $WORK1"
echo "2) $WORK2"
echo "3) $WORK3"
echo "4) $WORK4"
echo "5) $WORK5"
echo "6) $WORK6"
echo "7) $WORK7"
echo "8) $WORK8"
echo "9) $WORK9"
echo "10) $WORK10"
read -p "Введите номер (1-10): " choice

# Выбираем скрипт на основе пользовательского ввода
case $choice in
    1) selected_script="$WORK1" ;;
    2) selected_script="$WORK2" ;;
    3) selected_script="$WORK3" ;;
    4) selected_script="$WORK4" ;;
    5) selected_script="$WORK5" ;;
    6) selected_script="$WORK6" ;;
    7) selected_script="$WORK7" ;;
    8) selected_script="$WORK8" ;;
    9) selected_script="$WORK9" ;;
    10) selected_script="$WORK10" ;;
    *) echo "Неверный выбор. Пожалуйста, введите число от 1 до 10."; exit 1 ;;
esac

# Проверяем наличие выбранного скрипта перед запуском
if check_script "$selected_script"; then
    echo "Запускаем $selected_script"
    bash "$SCRIPTS_DIR/$selected_script"
else
    echo "Ошибка: Выбранный скрипт не найден. Выполнение прервано."
    exit 1
fi

