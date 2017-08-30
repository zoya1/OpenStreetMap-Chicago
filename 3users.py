import xml.etree.cElementTree as ET
import pprint
import re

def get_user(element):
    uid = ""
    if element.tag == "node" or element.tag == "way" or element.tag == "relation":
        uid = element.get('uid')
    return uid



def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        if get_user(element):
            users.add(get_user(element))
    return users

def test():

    users = process_map('chicago_il.osm')
    pprint.pprint(users)

if __name__ == "__main__":
    test()
