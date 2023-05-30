#!/usr/bin/python3
'''
This script contains a flask web appilcation set up
'''
from os import getenv
from flask import Flask

from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app_host = getenv('HBNB_API_HOST', '0.0.0.0')
app_port = int(getenv('HBNB_API_PORT', '5000'))
app.url_map.strict_slashes = False
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_flask(exception):
    '''The Flask request context and event listener.'''
    # print(exception)
    storage.close()





if __name__ == '__main__':
    app_host = getenv('HBNB_API_HOST', '0.0.0.0')
    app_port = int(getenv('HBNB_API_PORT', '5000'))
    app.run(
        host=app_host,
        port=app_port,
        threaded=True
    )
