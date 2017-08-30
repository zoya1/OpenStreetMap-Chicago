import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "chicago_il.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road",
            "Trail", "Parkway", "Commons"]

# UPDATE THIS VARIABLE
mapping = { "St": "Street",
            "St.": "Street",
            "Rd.": "Road",
            "Rd" : "Road",
            "Ave": "Avenue",
            "Ave.": "Avenue",
            "Avebue" : "Avenue",
            "Ln" : "Lane",
            "Ln." : "Lane",
            "chicago" : "Chicago",
            "ave" : "Avenue",
            "Dr" : "Drive",
            "Dr." : "Drive",
            "Cir" : "Circle",
            "Ct." : "Court",
            "Ct" : "Court",
            "Pl": "Place",
            "Pl.": "Place",
            "PKWY": "Parkway"
            }


def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)
    return street_types


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types
pprint.pprint(dict(audit(OSMFILE))) # this prints existing street names

 #return updated street names

def update_name(name, mapping):
    m = street_type_re.search(name)
    better_name = name
    if m:
        if m.group() in mapping.keys():
            better_street_type = mapping[m.group()]
            better_name = street_type_re.sub(better_street_type, name)
    return better_name

def test():
    street_types = audit(OSMFILE)
    pprint.pprint(dict(street_types))

    for street_type, ways in street_types.iteritems():
        for name in ways:
            better_name = update_name(name, mapping)
            print name, "=>", better_name

if __name__ == '__main__':
    test()
