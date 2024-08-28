#!/usr/bin/env python3

import os
import sqlite3
import curses
from curses import wrapper
from subprocess import Popen

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
    "start_dbv_postgres.sh":              "Запуск проекта dbv_postgres",
    "start_db_tlds_timescaledb.sh":       "Запуск проекта db_tlds_timescaledb",
    "start_db_tlds_questdb.sh":           "Запуск проекта db_tlds_questdb",
    "start_compose_go.sh":                "Запуск compose with go - start_compose_go",
    "start_ivldm.sh":                     "Запуск проекта IVLDM (сайт IVL document manager) на основе SQLite",
    "start_quesrdb_test.sh":              "Запуск теста работы questdb вместе с app.py",
    "start_app_to_postgres.sh":           "Запуск проекта работы postgresql в контейнере на уд. VM(Vital)",
    "start_html_bootstrap_js.sh":         "Запуск проекта с сервером сайта на bootstrap",
}

# Функция для логирования выполнения скрипта в базу данных
def log_script_execution(script_name):
    conn = sqlite3.connect('script_history.db')
    c = conn.cursor()
    c.execute('INSERT INTO history (script_name) VALUES (?)', (script_name,))
    conn.commit()
    conn.close()

# Функция для запуска скрипта
def run_script(script_name):
    script_path = os.path.join(SCRIPTS_DIR, script_name)
    if os.path.isfile(script_path):
        Popen(["bash", script_path])
        log_script_execution(script_name)
    else:
        print(f"Скрипт {script_name} не найден.")

# Функция для отрисовки меню
def draw_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, (script, description) in enumerate(scripts.items()):
        menu_text = f"{idx + 1}. {description}"
        x = 1  # Отступ по табуляции
        y = h//2 - len(scripts)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, menu_text)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, menu_text)
    # Печать пустой строки внизу для маркера
    stdscr.addstr(h-1, 1, "Выберите скрипт и нажмите Enter. Для выхода нажмите Ctrl-C.")
    stdscr.refresh()

# Основная функция
def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    current_row = 0

    draw_menu(stdscr, current_row)

    while True:
        try:
            key = stdscr.getch()

            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(scripts) - 1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                script_name = list(scripts.keys())[current_row]
                run_script(script_name)
                # Переместить маркер в пустую строку внизу после выполнения
                current_row = len(scripts)
            elif key == 3:  # Ctrl-C
                break

            draw_menu(stdscr, current_row)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    wrapper(main)

