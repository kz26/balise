# WSGI wrapper for standard reverse proxy setups
# http://flask.pocoo.org/docs/0.10/deploying/wsgi-standalone/#proxy-setups

from werkzeug.contrib.fixers import ProxyFix
from main import app


app.wsgi_app = ProxyFix(app.wsgi_app)
