from flask import Flask,render_template,jsonify,send_from_directory,safe_join,send_file,request
from collections import OrderedDict
from os.path import join

app = Flask(__name__)

# default config
app.config.from_pyfile('default_config.py')
# bonus config
app.config.from_envvar('ROMFILTER_SETTINGS',silent=True)

from .generate_gamelist import get_games
from .rommanager import in_store,copy_rom
ugames = get_games(app.config['MAME_CTLDB'],app.config.get('MAMECACHE'))
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
        if request.headers['Content-Type'] == 'application/json':
            return jsonify(g)
        else:
            return render_template("gameinfo.html",game=game,deployed=g['deployed'] )
    else:
        return "no such game",404

@app.route('/<game>/title')
def gametitle(game):
    if game in games:
        try:
            title=safe_join(join(app.config['SYNC_ARCHIVEDIR'],"title"),game+".png")
            print(title)
            return send_file(title)
        except Exception as e:
            print(e)
            return app.send_static_file('img/404-title.png')
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
