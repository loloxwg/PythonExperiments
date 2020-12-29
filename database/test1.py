import sqlite3

conn = sqlite3.connect('ex.db')

c = conn.cursor()

# c.execute('''create table stocks (data text ,trans text ,symbol text ,qty real,price real)''')
# #
# c.execute("insert into stocks values ('2016-1-1','buy','rhat','100','35.14')")


for row in c.execute('select * from stocks order by princ'):
    print(row)
conn.commit()

conn.close()
