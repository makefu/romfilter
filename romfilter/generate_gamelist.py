#!/usr/bin/env python

import pickle
def write_cache(dbfile,cachefile):
    games = gen_from_mamedb(dbfile,None)

    with open(cachefile,"bw+") as c:
        pickle.dump(games,c)

def load_cache(cachefile):
    with open(cachefile,"rb") as c:
        return pickle.load(c)


def gen_from_mamedb(dbfile,cachefile=None):
    import xml.etree.ElementTree as ET
    tree = ET.parse(dbfile)
    root = tree.getroot()
    games= {}

    try: return load_cache(cachefile)
    except Exception as e:print(e)

    for game in tree.findall('game'):
        if game.attrib.get('isbios'): continue
        if game.attrib.get('cloneof'): continue
        if game.attrib.get('isdevice'): continue
        if game.attrib.get('ismechanical'): continue
        ng = {}
        ng['name'] = game.find('description').text
        try: ng['year'] = game.find('year').text
        except: ng['year'] = 'unknown'
        try: ng['manufacturer'] = game.find('manufacturer').text
        except: ng['manufacturer'] = 'unknown'
        games[game.attrib['name']] = ng
    return games

