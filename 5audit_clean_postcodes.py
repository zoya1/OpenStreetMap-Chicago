import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint


osmfile = "chicago_il.osm"

def is_postcode(elem):
    return (elem.attrib['k'] == "addr:postcode")


def audit_postcode(invalid_postcodes, postcode):
    first_two_digit = postcode[:2]
    if len(postcode)!= 5:
        invalid_postcodes.append(postcode)
    elif first_two_digit not in ['60']:
        invalid_postcodes.append(postcode)
    elif not postcode.isdigit():
        invalid_postcodes.append(postcode)


def audit(osmfile):
    osm_file = open(osmfile, "r")
    invalid_postcodes = []
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"): #return all the subtags named "tag" nested within this element
                if is_postcode(tag):
                    audit_postcode(invalid_postcodes, tag.attrib['v'])

    osm_file.close()
    return invalid_postcodes


invalid_postcodes = audit(osmfile)

def test():
    invalid_postcodes = audit(osmfile)

    pprint.pprint(invalid_postcodes)
if __name__ == '__main__':
    test()


test = ['60513-9998',
 '60660-4199',
 '60077-3495',
 '60521-2101',
 '60016-5608',
 '60016-5670',
 '60077-3495',
 '60521-2101',
 '60016-5608',
 '60016-5670',
 '60615-5299',
 '60654-5799',
 '60712-2716',
 '60076-2000',
 '60077-1314',
 '60660-4199',
 '60160-1607',
 '60622-4580',
 '60546-1262',
 '2300',
 '6074',
 '60614 ',
 '0201',
 '606226',
 '690639',
 '46320',
 '606',
 '2300',
 '6017',
 '6051',
 '6074',
 '60614 ',
 '46327',
 'IL',
 'IL, 60642',
 'IL, 60126',
 'IL 60707',
 'IL 60605-1226',
 '60654-5799',
 '60827-6427',
 '60018-2627',
 '46320',
 '46312',
 '46321',
 '46394'
  ]

def update_postcode(postcode):
    # new regular expression pattern
    search = re.match(r'^\D*(6\d{4}).*', postcode)
    #select the group that is captured
    if search:
        clean_postcode = search.group(1)
        return clean_postcode
for item in test:
    cleaned = update_postcode(item)
    print cleaned
    
