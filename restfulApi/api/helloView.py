from restfulApi.app import app
from flask import make_response, redirect, url_for, abort, jsonify
from restfulApi.model.Music import Music
from restfulApi.model.Artist import Artist


@app.route('/')
def home():
    musics = Music.query.order_by(Music.publish_time.desc()).all()
    artists = Artist.query.order_by(Artist.id.desc()).all()
    ret = {
        'music': [m.serialize() for m in musics],
        'artist': [m.serialize() for m in artists]
    }
    return jsonify(ret=ret)


@app.route("/hello")
def hello():
    return 'hello'


@app.route("/hello1")
def hello1():
    return 'hello1', 200, {'name': 'victory'}


@app.route("/hello2")
def hello2():
    return 'hello2', 200


@app.route("/hello3")
def hello3():
    response = make_response()
    response.set_cookie()
    return redirect(url_for('hello1'))


@app.route("/404")
def hello404():
    abort(404)


@app.teardown_appcontext
def teardown_db(exception):
    # 程序上下文销毁时调用
    if exception is not None:
        print("teardown_db %s" % exception.__str__())
    ...
