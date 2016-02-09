#!/usr/bin/env python

import pickle
def write_cache(games,cachefile):

    with open(cachefile,"bw+") as c:
        pickle.dump(games,c)
    return games

def load_cache(cachefile):
    with open(cachefile,"rb") as c:
        return pickle.load(c)


def get_games(dbfile,cachefile=None):
    if cachefile:  #cache file given
        # try to load the old cache
        try: return load_cache(cachefile)
        except Exception as e:print(e)

        # or write a new cache, invokes gen_from_mamectl
        games = gen_from_mamectl(dbfile)
        return write_cache(games,cachefile)
    else: #no cache file given, generate a new games db
        return gen_from_mamectl(dbfile)


def gen_from_mamectl(dbfile):
    import xml.etree.ElementTree as ET
    tree = ET.parse(dbfile)
    root = tree.getroot()
    games= {}

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
    # write a cache file if we were not able to load from it before
    return games
