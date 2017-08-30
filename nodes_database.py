import sqlite3
import csv
from pprint import pprint

sqlite_file = 'mydb.db' # sqlite database

#conn - connect to the database
conn = sqlite3.connect(sqlite_file)

#create a cursor object
cur = conn.cursor()

#Before you (re)create the table, you will have to drop the table if it already exists:
cur.execute('''DROP TABLE IF EXISTS nodes''')
conn.commit()

#create the table, specifying column names and data types
cur.execute('''
    CREATE TABLE nodes(id INTEGER PRIMARY KEY NOT NULL, lat REAL, lon REAL, user TEXT, uid INTEGER, version INTEGER, changeset INTEGER, timestamp TEXT)
''')

conn.commit()

# Read in the csv file as a dictionary, format the
# data as a list of tuples:
with open('nodes.csv','rb') as fin:
    dr = csv.DictReader(fin)
    to_db = [(i['id'], i['lat'], i['lon'], i['user'].decode("utf-8"), i['uid'], i['version'], i['changeset'], i['timestamp']) for i in dr]


#insert formatted data
cur.executemany("INSERT INTO nodes(id, lat, lon, user, uid, version, changeset, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?, ?);", to_db)
# commit the changes
conn.commit()

cur.execute('SELECT * FROM nodes')
all_rows = cur.fetchall()
print('5):')
#pprint(all_rows)

conn.close()
