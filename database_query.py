import sqlite3
import csv
from pprint import pprint
sqlite_file = 'mydb.db' # sqlite database
#conn - connect to the database
conn = sqlite3.connect(sqlite_file)
#create a cursor object
cur = conn.cursor()

#Number of nodes
cur.execute('SELECT COUNT (*) FROM nodes')
all_rows = cur.fetchall()
print ('1):')
pprint(all_rows)

#Number of ways
cur.execute('SELECT COUNT (*) FROM ways')
all_rows = cur.fetchall()
print ('1):')
pprint(all_rows)

#Total number of users
cur.execute('''SELECT COUNT (*) as num
FROM (SELECT user FROM nodes UNION ALL
SELECT user FROM ways)''')
all_rows = cur.fetchall()
print ('1):')
pprint(all_rows)

#Top contributing users
cur.execute('''SELECT user, COUNT(*) as num
FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways)
GROUP BY user
ORDER BY num DESC
LIMIT 10;''')
all_rows = cur.fetchall()
print('1):')
pprint(all_rows)

#number of distinct/uniue users
cur.execute('''SELECT COUNT (DISTINCT uid)
FROM (SELECT uid FROM nodes UNION ALL SELECT uid FROM ways);''')
all_rows = cur.fetchall()
pprint(all_rows)

#number of onetime contributors
cur.execute('''SELECT COUNT(*)
FROM
(SELECT user, COUNT (*) as num
FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways)
GROUP BY user
Having num = 1) ;''')
all_rows = cur.fetchall()
print(all_rows)

#common ammenities
cur.execute('''SELECT value, COUNT(*)as num
FROM nodes_tags
WHERE key = 'amenity'
GROUP BY value
ORDER BY num DESC
LIMIT 10;''')
all_rows = cur.fetchall()
print('1):')
pprint(all_rows)

#cuisine
cur.execute('''SELECT value, COUNT (*) as num
FROM nodes_tags
WHERE key = 'cuisine'
GROUP BY value
ORDER BY num DESC
LIMIT 10;''')
all_rows = cur.fetchall()
print('1):')
pprint(all_rows)

#place of worship
cur.execute('''SELECT value, COUNT (*) as num
FROM nodes_tags
WHERE key = 'religion'
GROUP BY value
ORDER BY num DESC
LIMIT 10;''')
all_rows = cur.fetchall()
print('1):')
pprint(all_rows)
