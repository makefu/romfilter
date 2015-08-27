from flask import Flask

app = Flask(__name__)

# default config
app.config.from_pyfile('default_config.py')
# bonus config
app.config.from_envvar('ROMFILTER_SETTINGS',silent=True)

