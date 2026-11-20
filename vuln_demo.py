import sqlite3

def get_user(db_path, username):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # Deliberately flaggable: SQL built by string formatting.
    cur.execute("SELECT * FROM users WHERE name = '%s'" % username)
    return cur.fetchall()
