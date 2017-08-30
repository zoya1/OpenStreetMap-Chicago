import sqlite3
import csv
from pprint import pprint

sqlite_file = 'mydb.db' # sqlite database

#conn - connect to the database
conn = sqlite3.connect(sqlite_file)

#create a cursor object
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS nodes_tags''')
conn.commit()

cur.execute('''
    CREATE TABLE nodes_tags(id INTEGER, key TEXT, value TEXT, type TEXT, FOREIGN KEY (id) REFERENCES nodes(id))
''')
conn.commit()

with open('nodes_tags.csv','rb') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['id'], i['key'], i['value'].decode("utf-8"), i['type']) for i in dr]

cur.executemany("INSERT INTO nodes_tags(id, key, value, type) VALUES (?, ?, ?, ?);", to_db)
# commit the changes
conn.commit()

cur.execute('SELECT * FROM nodes_tags')
all_rows = cur.fetchall()
print('1):')
#pprint (all_rows)

conn.close()
