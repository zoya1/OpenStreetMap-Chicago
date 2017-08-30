# Udacity-DAND
Exploratory analysis of OpenStreetMap of Chicago,IL

Files include :

Quiz : scripts submitted in Case Study OpenStreetMap

chicago_il.osm: original OSM file

sample.osm: sample OSM file derived from chicago_il.osm

report.pdf : report

0sample.py : extract sample data and outputs sample.osm from OSM file

1mapparser.py : finds tags in the data

2tag_types.py : counts different tags 

3users.py : gives user information

4audit_clean_street.py : audits and cleans street names

5audit_clean_postcodes.py : audits and cleans postal codes

6data.py : builds 5 different CSV files in from original OSM file and also parses, cleanses data

database : Contains five .py scripts used in connecting 5 csv files to SQLite database mydb.db

mydb.db : SQLite database

database_query.py : SQL queries used to explore data

schema.py : schema followed to create csv files after audit and cleaning of data

