import os
import sys

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

# config db
app = Flask('restfulApi')
if sys.platform.startswith('win'):
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from restfulApi import command, views

if __name__ == '__main__':
    app.run()


@app.before_request
def before_request():
    # print("method: %s, header: %s" % (request.method, request.headers.environ))
    print("method: %s, url: %s, cookie: %s, values: %s, data: %s" % (request.method, request.url,
                                                                     request.cookies, request.values, request.data))
