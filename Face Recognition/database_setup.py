import sqlite3

con = sqlite3.connect("Blackout.db")
cur = con.cursor()
cur.execute("CREATE TABLE users(name, secret_key)")
