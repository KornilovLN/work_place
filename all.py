#!/usr/bin/env python3

import os
import subprocess

# Константа для пути к скриптам
SCRIPTS_DIR = 'scripts'

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

def run_scripts(scripts):
    for script in scripts:
        full_path = os.path.join(SCRIPTS_DIR, script)
        if os.path.isfile(full_path):
            try:
                subprocess.run(["bash", full_path], check=True)
                print(f"\nСкрипт {script} успешно выполнен.")
            except subprocess.CalledProcessError as e:
                print(f"\nОшибка при выполнении скрипта {script}: {e}")
        else:
            print(f"\nСкрипт {script} не найден и не был выполнен.")

def main():
    about()

    scripts = [
        "docker_spd-project_8082.sh",
        "sunpp_python_8083.sh",
        #"sunpp_docs_python_8083.sh",
        #"sunpp_npx_8086.sh",
        #"sunpp_docs_npx_8086.sh",
        #"ivl_site_8088.sh",
        #"ekatra_flask_8089.sh",
        "poligon_ekatra_flask_8089.sh",
        "app_to_postgres.sh",               #5000
    ]

    check_scripts(scripts)
    run_scripts(scripts)

if __name__ == "__main__":
    main()

