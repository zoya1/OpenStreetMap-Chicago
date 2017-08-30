import sqlite3
import csv
from pprint import pprint

sqlite_file = 'mydb.db' # sqlite database

#conn - connect to the database
conn = sqlite3.connect(sqlite_file)

#create a cursor object
cur = conn.cursor()

#Before you (re)create the table, you will have to drop the table if it already exists:
cur.execute('''DROP TABLE IF EXISTS ways_nodes''')
conn.commit()

#create the table, specifying column names and data types
cur.execute('''
    CREATE TABLE ways_nodes(id INTEGER NOT NULL, node_id INTEGER NOT NULL, position INTEGER NOT NULL, FOREIGN KEY (id) REFERENCES ways(id), FOREIGN KEY (node_id) REFERENCES nodes(id))
''')
conn.commit()

# Read in the csv file as a dictionary, format the
# data as a list of tuples:
with open('ways_nodes.csv','rb') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['id'], i['node_id'], i['position']) for i in dr]

#insert formatted data
cur.executemany("INSERT INTO ways_nodes(id, node_id, position) VALUES (?, ?, ?);", to_db)
# commit the changes
conn.commit()

cur.execute('SELECT * FROM ways_nodes')
all_rows = cur.fetchall()
print('1):')
#pprint (all_rows)

conn.close()
