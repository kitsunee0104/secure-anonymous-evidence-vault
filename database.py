import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "evidence.db")

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS evidence (
            case_id TEXT PRIMARY KEY,
            file_hash TEXT NOT NULL,
            file_path TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def store_file(case_id, file_hash, file_path):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO evidence (case_id, file_hash, file_path) VALUES (?, ?, ?)",
        (case_id, file_hash, file_path)
    )
    conn.commit()
    conn.close()

