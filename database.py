import sqlite3
PATH = 'db.database'
conn = sqlite3.connect(PATH)
cur = conn.cursor()
