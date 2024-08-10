#!/usr/bin/env python3

import os
import subprocess

# Константа для пути к скриптам
SCRIPTS_DIR = 'scripts'

# Максимальное количество скриптов для вызова
MAX_CHOISE=5

def about():
    print(
    '''
    -----------------------------------------------------------
    Программа запуска скриптов, стартующих документы в браузере
    сustomer: IVL Equipment & Engineering
    -----------------------------------------------------------
    author: Старых ЛН
    e-mail: ln.kornilovstar@gmail.com
    e-mail: ln.starmark@ekatra.io
    github: https://github.com/KornilovLN
    tel:    +380 66 9805661
    ------------------------------------------------------------
    ''')

def check_scripts(scripts):    
    for script in scripts:
        full_path = os.path.join(SCRIPTS_DIR, script)
        if not os.path.isfile(full_path):
            print(f"Ошибка: Скрипт {script} не найден.")
        else:
            print(f"Скрипт {script} найден.")

def get_user_choice(scripts):
    print("\nКакой скрипт вы хотите запустить?")
    for i, script in enumerate(scripts, 1):
        print(f"{i}) {script}")

    while True:
        try:
            choice = int(input("\nВведите номер: 1-5: "))
            if 1 <= choice <= MAX_CHOISE:
                return choice
            else:
                print("Пожалуйста, введите число от 1 до ", end="")
                print(MAX_CHOISE)
        except ValueError:
            print("Пожалуйста, введите корректное число.")

def run_script(script):
    full_path = os.path.join(SCRIPTS_DIR, script)
    try:
        subprocess.run(["bash", full_path], check=True)
        print(f"\nСкрипт {script} успешно выполнен.")
    except subprocess.CalledProcessError as e:
        print(f"\nОшибка при выполнении скрипта {script}: {e}")

    print(f"\nСкрипт {script} {'найден' if os.path.isfile(full_path) else 'не найден'} после попытки запуска.")

def main():
    about()

    scripts = [
        "docker_spd-project_8082.sh",
        "sunpp_python_8083.sh",
        #"sunpp_docs_python_8083.sh",
        "sunpp_npx_8086.sh",
        #"sunpp_docs_npx_8086.sh",
        "ivl_site_8088.sh",
        "ekatra_flask_8089.sh",
    ]

    check_scripts(scripts)
    choice = get_user_choice(scripts)
    selected_script = scripts[choice - 1]
    run_script(selected_script)

if __name__ == "__main__":
    main()



