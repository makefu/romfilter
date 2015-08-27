from flask import Flask,render_template,jsonify

app = Flask(__name__)

# default config
app.config.from_pyfile('default_config.py')
# bonus config
app.config.from_envvar('ROMFILTER_SETTINGS',silent=True)

from .generate_gamelist import gen_from_mamedb
games = gen_from_mamedb(app.config['MAMEDB'])

@app.route('/')
def index():
    return render_template('static.html',games=games)

@app.route('/all_games')
def all_games():
    # TODO: mame version from db?
    return jsonify({"games":games})


if __name__ == '__main__':
    app.run()
