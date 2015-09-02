from flask import Flask,render_template,jsonify
from collections import OrderedDict


app = Flask(__name__)

# default config
app.config.from_pyfile('default_config.py')
# bonus config
app.config.from_envvar('ROMFILTER_SETTINGS',silent=True)

from .generate_gamelist import gen_from_mamedb
from .rommanager import in_store,copy_rom
ugames = gen_from_mamedb(app.config['MAMEDB'],app.config.get('MAMECACHE'))
games = OrderedDict(sorted(ugames.items()))

@app.route('/')
def index():
    return render_template('romlist.html')

@app.route('/all_games')
def all_games():
    # TODO: mame version from db?
    return jsonify(games)

@app.route('/<game>/info')
def gameinfo(game):
    # TODO: mame version from db?
    if game in games:
        g = games[game]
        g['deployed'] = in_store(app.config['SYNC_LIVEDIR'],game)
        return jsonify(g)
    else:
        return "no such game",404

@app.route('/<game>/add')
def addgame(game):
    if game in games:
        gameinfo = games[game]
        try:
            copy_rom(app.config['SYNC_LIVEDIR'],app.config['SYNC_ARCHIVEDIR'],game)
            return "success"
        except:
            return "failure", 500
    else:
        return "no such game",404


if __name__ == '__main__':
    app.run()
