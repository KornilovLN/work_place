#!/bin/bash

# Константа для пути к скриптам
SCRIPTS_DIR="works"

# Массив имен скриптов
scripts=(
    "start_work_tree_node.sh"
    "start_work_folder_site.sh"
    "start_comment_sunpp.sh"
    "docker_simple_docs.sh"
    "claster_work_start.sh"
    "start_install_sunpp_2vm.sh"
    "start_install_sunpp_2_vm-docker.sh"
    "start_multi_dockers.sh"
    "start_multi_vm_gen_db_view_repo.sh"
    "start_for_ekatra_test.sh"
)

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

# Цикл для проверки наличия каждого скрипта
for script in "${scripts[@]}"; do
    check_script "$script"
done

echo -e "\nКакой скрипт вы хотите запустить?"

# Вывод списка скриптов с номерами
for i in "${!scripts[@]}"; do
    printf "%d) %s\n" "$((i+1))" "${scripts[$i]}"
done

read -p "Введите номер (1-${#scripts[@]}): " choice

# Выбираем скрипт на основе пользовательского ввода
if ((choice >= 1 && choice <= ${#scripts[@]})); then
    selected_script="${scripts[$((choice-1))]}"

    # Проверяем наличие выбранного скрипта перед запуском
    if check_script "$selected_script"; then
        echo "Запускаем $selected_script"
        bash "$SCRIPTS_DIR/$selected_script"
    else
        echo "Ошибка: Выбранный скрипт не найден. Выполнение прервано."
        exit 1
    fi
else
    echo "Неверный выбор. Пожалуйста, введите число от 1 до ${#scripts[@]}."
    exit 1
fi

