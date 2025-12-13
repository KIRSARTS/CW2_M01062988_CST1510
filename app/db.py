import sqlite3

def get_db_connection():
    conn = sqlite3.connect('DATA/intelligence_platform.db', check_same_thread=False)
    return conn
