import sqlite3

con = sqlite3.connect("Blackout.db")
cur = con.cursor()
cur.execute("CREATE TABLE users(name, secret_key)")
con.commit()  # Save the changes
con.close()  # Close the connection
