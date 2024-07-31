#!/usr/bin/env python3

import os

# Константа для пути к скриптам
SCRIPTS_DIR = "works"

# Словарь скриптов
scripts = {
    "start_work_tree_node.sh":            "Запуск рабочего дерева узлов",
    "start_work_folder_site.sh":          "Запуск рабочей папки сайта",
    "start_comment_sunpp.sh":             "Запуск комментариев SUNPP",
    "docker_simple_docs.sh":              "Простая документация Docker",
    "claster_work_start.sh":              "Запуск работы кластера",
    "start_install_sunpp_2vm.sh":         "Установка SUNPP на 2 VM",
    "start_install_sunpp_2_vm-docker.sh": "Установка SUNPP на 2 VM с Docker",
    "start_multi_dockers.sh":             "Запуск нескольких Docker контейнеров",
    "start_multi_vm_gen_db_view_repo.sh": "Запуск нескольких VM с генерацией БД и просмотром репозитория",
    "start_for_ekatra_test.sh":           "Запуск теста для Ekatra",
    "start_gbv_mongodb.sh":               "Запуск проекта с генератором, MongoDB и вьювером",
    "start_ekatra_flask.sh":              "Запуск проекта сайта ekatra_flask",
    "start_work_rabbitmq.sh":             "Запуск проекта rabbitmq",
}

def about():
    print(
    '''
    -----------------------------------------------------------
    Программа запуска скриптов, стартующих work-userspace
    сustomer: IVL Equipment & Engineering
    -----------------------------------------------------------
    author: Старых ЛН
    e-mail: ln.kornilovstar@gmail.com
    e-mail: ln.starmark@ekatra.io
    github: https://github.com/KornilovLN
    tel:    +380 66 9805661
    ------------------------------------------------------------
    ''')

def check_script(script_name):
    script_path = os.path.join(SCRIPTS_DIR, script_name)
    if os.path.isfile(script_path):
        #print(f"Скрипт {script_name} найден.")
        return True
    else:
        print(f"Скрипт {script_name} не найден.")
        return False

def print_scripts_list():
    print("\nКакой скрипт вы хотите запустить?")
    for i, (script, description) in enumerate(scripts.items(), start=1):
        print(f"{i}) {description} ({script})")

def get_user_choice():
    choice = int(input(f"Введите номер (1-{len(scripts)}): "))
    return choice

def run_selected_script(choice):
    if 1 <= choice <= len(scripts):
        selected_script = list(scripts.keys())[choice - 1]
        if check_script(selected_script):
            print(f"Запускаем {scripts[selected_script]} ({selected_script})")
            script_path = os.path.join(SCRIPTS_DIR, selected_script)
            os.system(f"bash {script_path}")
        else:
            print("Ошибка: Выбранный скрипт не найден. Выполнение прервано.")
    else:
        print(f"Неверный выбор. Пожалуйста, введите число от 1 до {len(scripts)}.")

def main():
    about()
    print("Проверка наличия скриптов:")
    for script in scripts:
        check_script(script)
    print_scripts_list()
    choice = get_user_choice()
    run_selected_script(choice)

if __name__ == "__main__":
    main()

