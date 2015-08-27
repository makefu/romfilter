#!/usr/bin/env python

def gen_from_mamedb(dbfile):
    import xml.etree.ElementTree as ET
    tree = ET.parse(dbfile)
    root = tree.getroot()
    games= []
    for game in tree.findall('game'):
        if game.attrib.get('isbios'): continue
        if game.attrib.get('cloneof'): continue
        if game.attrib.get('isdevice'): continue
        if game.attrib.get('ismechanical'): continue
        ng = {}
        ng['short'] = game.attrib['name']
        ng['name'] = game.find('description').text
        try: ng['year'] = game.find('year').text
        except: ng['year'] = 'unknown'
        try: ng['manufacturer'] = game.find('manufacturer').text
        except: ng['manufacturer'] = 'unknown'
        games.append(ng)
    return games

