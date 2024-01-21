import sqlite3
weap = input()
con = sqlite3.connect("db_for_attack")
cur = con.cursor()
result = cur.execute("""SELECT * FROM for_attack WHERE weapon = ?""", (weap,)).fetchone()
for elem in result:
    print(elem)
con.close()