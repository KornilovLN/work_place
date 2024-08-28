#!/usr/bin/env python3

import sqlite3

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

if __name__ == "__main__":
    init_db()

