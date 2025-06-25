import sqlite3
from pathlib import Path
from datetime import datetime

DB_PATH = Path.cwd() / "launchhub.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS project_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            stack TEXT NOT NULL,
            path TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

def log_project(name, stack, path):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    c.execute('''
        INSERT INTO project_log (name, stack, path, created_at)
        VALUES (?, ?, ?, ?)
    ''', (name, stack, str(path), timestamp))

    conn.commit()
    conn.close()

def list_projects():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("SELECT name, stack, path, created_at FROM project_log ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()

    if not rows:
        print("No projects found.")
        return

    print("\n🔍 Project Log:\n")
    for row in rows:
        print(f"- [{row[3]}] {row[0]} ({row[1]}) → {row[2]}")
