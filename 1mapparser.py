import xml.etree.cElementTree as ET
import pprint
import re
import csv
import codecs



#this function counts the number of node,way and relation tags present in the sample file
def count_tags(filename):
    tags = {}
    for event, elem in ET.iterparse(filename):
        if elem.tag in tags.keys():
            tags[elem.tag]+= 1
        else:
            tags[elem.tag] = 1
    return tags

count_tags('chicago_il.osm')
