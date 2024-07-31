#!/usr/bin/env python3

import os

# Константа для пути к скриптам
SCRIPTS_DIR = "works"

# Массив имен скриптов
scripts = [
    "start_work_tree_node.sh",
    "start_work_folder_site.sh",
    "start_comment_sunpp.sh",
    "docker_simple_docs.sh",
    "claster_work_start.sh",
    "start_install_sunpp_2vm.sh",
    "start_install_sunpp_2_vm-docker.sh",
    "start_multi_dockers.sh",
    "start_multi_vm_gen_db_view_repo.sh",
    "start_for_ekatra_test.sh"
]

# Функция для проверки наличия скрипта
def check_script(script_name):
    script_path = os.path.join(SCRIPTS_DIR, script_name)
    if os.path.isfile(script_path):
        print(f"Скрипт {script_name} найден.")
        return True
    else:
        print(f"Скрипт {script_name} не найден.")
        return False

print("Проверка наличия скриптов:")

# Цикл для проверки наличия каждого скрипта
for script in scripts:
    check_script(script)

print("\nКакой скрипт вы хотите запустить?")

# Вывод списка скриптов с номерами
for i, script in enumerate(scripts, start=1):
    print(f"{i}) {script}")

choice = int(input(f"Введите номер (1-{len(scripts)}): "))

# Выбираем скрипт на основе пользовательского ввода
if 1 <= choice <= len(scripts):
    selected_script = scripts[choice - 1]

    # Проверяем наличие выбранного скрипта перед запуском
    if check_script(selected_script):
        print(f"Запускаем {selected_script}")
        script_path = os.path.join(SCRIPTS_DIR, selected_script)
        os.system(f"bash {script_path}")
    else:
        print("Ошибка: Выбранный скрипт не найден. Выполнение прервано.")
else:
    print(f"Неверный выбор. Пожалуйста, введите число от 1 до {len(scripts)}.")

