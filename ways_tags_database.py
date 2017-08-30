import sqlite3
import csv
from pprint import pprint

sqlite_file = 'mydb.db' # sqlite database

#conn - connect to the database
conn = sqlite3.connect(sqlite_file)

#create a cursor object
cur = conn.cursor()

#Before you (re)create the table, you will have to drop the table if it already exists:
cur.execute('''DROP TABLE IF EXISTS ways_tags''')
conn.commit()

#create the table, specifying column names and data types
cur.execute('''
    CREATE TABLE ways_tags(id INTEGER NOT NULL, key TEXT NOT NULL, value TEXT NOT NULL, type TEXT, FOREIGN KEY (id) REFERENCES ways(id))
''')

conn.commit()

# Read in the csv file as a dictionary, format the
# data as a list of tuples:
with open('ways_tags.csv','rb') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['id'], i['key'], i['value'].decode("utf-8"), i['type']) for i in dr]

#insert formatted data
cur.executemany("INSERT INTO ways_tags(id, key, value, type) VALUES (?, ?, ?, ?);", to_db)
# commit the changes
conn.commit()
cur.execute('SELECT * FROM ways_tags')
all_rows = cur.fetchall()
print('1):')
#pprint (all_rows)

conn.close()
