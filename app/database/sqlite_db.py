import sqlite3
import os
from typing import Optional

# Update BASE_DIR to refer to the project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Now it will point to the project root
DB_NAME = os.path.join(BASE_DIR, "storage", "hash_store.db")

def get_connection():
    os.makedirs(os.path.dirname(DB_NAME), exist_ok=True)  # 🔧 Auto-create folder if missing
    return sqlite3.connect(DB_NAME)

def initialize_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS file_hashes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                hash TEXT UNIQUE,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

def insert_or_update_hash(hash_value: str):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO file_hashes (hash)
            VALUES (?)
            ON CONFLICT(hash) DO UPDATE SET
                timestamp = CURRENT_TIMESTAMP
        ''', (hash_value,))
        conn.commit()

def check_for_hash(hash_value: str) -> bool:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT 1 FROM file_hashes WHERE hash = ? LIMIT 1', (hash_value,))
        result = cursor.fetchone()
        return result is not None