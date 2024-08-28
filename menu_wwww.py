#!/usr/bin/env python3

import os
import sqlite3
import curses
from curses import wrapper
from subprocess import Popen
from datetime import datetime

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

# Функция для инициализации базы данных
def init_db():
    conn = sqlite3.connect('script_history_w.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY,
            script_name TEXT,
            date TEXT,
            count INTEGER,
            times TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Функция для логирования выполнения скрипта в базу данных
def log_script_execution(script_name):
    conn = sqlite3.connect('script_history_w.db')
    c = conn.cursor()
    date_str = datetime.now().strftime('%Y-%m-%d')
    time_str = datetime.now().strftime('%H:%M:%S')
    # Проверка, существует ли запись для данного скрипта и даты
    c.execute('SELECT id, count, times FROM history WHERE script_name = ? AND date = ?', (script_name, date_str))
    row = c.fetchone()
    if row:
        # Обновление существующей записи
        id, count, times = row
        count += 1
        times = f"{times};{time_str}"
        c.execute('UPDATE history SET count = ?, times = ? WHERE id = ?', (count, times, id))
    else:
        # Вставка новой записи
        c.execute('INSERT INTO history (script_name, date, count, times) VALUES (?, ?, ?, ?)', (script_name, date_str, 1, time_str))
    conn.commit()
    conn.close()

# Функция для получения истории выполнения скриптов
def get_history():
    conn = sqlite3.connect('script_history_w.db')
    c = conn.cursor()
    c.execute('SELECT script_name, date, count, times FROM history ORDER BY date DESC, id DESC')
    history = c.fetchall()
    conn.close()
    return history

# Функция для запуска скрипта
def run_script(script_name):
    script_path = os.path.join(SCRIPTS_DIR, script_name)
    if os.path.isfile(script_path):
        Popen(["bash", script_path])
        log_script_execution(script_name)
    else:
        print(f"Скрипт {script_name} не найден.")

# Функция для отрисовки меню
def draw_menu(stdscr, selected_row_idx, history, history_idx, history_date_idx, active_column):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    menu_width = (3 * w) // 5

    NSTRTITLE = 10

    # Отрисовка информации о программе
    about_text = [
        "------------------------------------------------------------",
        "Программа запуска скриптов, стартующих work-userspace",
        "author: Старых ЛН",
        "e-mail: ln.kornilovstar@gmail.com",
        "github: https://github.com/KornilovLN",
        "tel:    +380 66 9805661",
        "------------------------------------------------------------"
    ]

    # Отрисовка заголовка
    stdscr.addstr(NSTRTITLE, 4, "Выбор темы и среды работы", curses.A_BOLD)



    for i, line in enumerate(about_text):
        stdscr.addstr(i + 2, w // 2 - len(line) // 2, line)

    # Отрисовка меню скриптов
    for idx, (script, description) in enumerate(scripts.items()):
        menu_text = f"{idx + 1}. {description}"
        x = 1  # Отступ по табуляции
        y = NSTRTITLE + 2 + idx  # Смещение вниз для информации о программе
        if y < h and x + len(menu_text[:menu_width-2]) < w:
            if idx == selected_row_idx and active_column == "left":
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, menu_text[:menu_width-2])
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, menu_text[:menu_width-2])

    # Отрисовка истории
    if history:
        history_dates = sorted(set([record[1] for record in history]), reverse=True)
        if history_date_idx < len(history_dates):
            selected_date = history_dates[history_date_idx]
            stdscr.addstr(NSTRTITLE, menu_width + 2, f"История за {selected_date}")
            filtered_history = [record for record in history if record[1] == selected_date]
            for idx, (script_name, date, count, times) in enumerate(filtered_history):
                last_time = times.split(';')[-1]
                script_name_formatted = (script_name[:30] + '..') if len(script_name) > 30 else script_name.ljust(30)
                history_text = f"{idx + 1:<3} {script_name_formatted} {count:<5} {last_time}"
                x = menu_width + 2
                y = NSTRTITLE + 2 + idx  # Смещение вниз для информации о программе
                if y < h and x + len(history_text[:menu_width-2]) < w:
                    if idx == history_idx and active_column == "right":
                        stdscr.attron(curses.color_pair(1))
                        stdscr.addstr(y, x, history_text[:menu_width-2])
                        stdscr.attroff(curses.color_pair(1))
                    else:
                        stdscr.addstr(y, x, history_text[:menu_width-2])
    stdscr.refresh()

# Функция для установки размера терминала
#def set_terminal_size():
#    os.system('printf "\033[8;38;132t"')

def set_terminal_size():
    # Заданные размеры
    required_height = 38
    required_width = 132

    # Получение текущих размеров окна терминала
    current_height, current_width = os.popen('stty size', 'r').read().split()
    current_height = int(current_height)
    current_width = int(current_width)

    # Проверка размеров и установка, если необходимо
    if current_height < required_height or current_width < required_width:
        os.system(f'printf "\033[8;{required_height};{required_width}t"')



# Основная функция
def main(stdscr):
    set_terminal_size()

    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    current_row = 0
    history_idx = 0
    history_date_idx = 0
    active_column = "left"

    #init_db()
    history = get_history()

    draw_menu(stdscr, current_row, history, history_idx, history_date_idx, active_column)

    while True:
        try:
            key = stdscr.getch()

            if active_column == "left":
                if key == curses.KEY_UP and current_row > 0:
                    current_row -= 1
                elif key == curses.KEY_DOWN and current_row < len(scripts) - 1:
                    current_row += 1
                elif key == curses.KEY_ENTER or key in [10, 13]:
                    script_name = list(scripts.keys())[current_row]
                    run_script(script_name)
                    history = get_history()
                    # Переместить маркер в пустую строку внизу после выполнения
                    current_row = len(scripts)
                elif key == 9:  # Tab
                    active_column = "right"
            elif active_column == "right":
                if key == curses.KEY_UP and history_idx > 0:
                    history_idx -= 1
                elif key == curses.KEY_DOWN and history_idx < len([record for record in history if record[1] == sorted(set([record[1] for record in history]), reverse=True)[history_date_idx]]) - 1:
                    history_idx += 1
                elif key == curses.KEY_ENTER or key in [10, 13]:
                    filtered_history = [record for record in history if record[1] == sorted(set([record[1] for record in history]), reverse=True)[history_date_idx]]
                    script_name = filtered_history[history_idx][0]
                    run_script(script_name)
                    history = get_history()
                elif key == 9:  # Tab
                    active_column = "left"

            draw_menu(stdscr, current_row, history, history_idx, history_date_idx, active_column)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    wrapper(main)

