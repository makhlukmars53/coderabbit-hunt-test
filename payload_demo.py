"""Payload flaggable untuk PR uji A6 — HANYA di repo uji milik sendiri.

Pola yang sengaja dibuat supaya review CodeRabbit PASTI menandainya pada
PR kontrol (tanpa .coderabbit.yaml pengecualian):
1. SQL string formatting (SQL injection).
2. Secret contoh AWS yang dipublikasi di dokumentasi AWS sebagai contoh
   (AKIAIOSFODNN7EXAMPLE) — BUKAN kredensial asli, tidak bisa dipakai.
"""
import sqlite3

AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"


def get_user(db_path, username):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE name = '%s'" % username)
    return cur.fetchall()
