from restfulApi import app, db
from restfulApi.model.Music import Music
from restfulApi.model.Artist import Artist
from flask import jsonify


@app.route('/music')
def music():
    musics = Music.query.order_by(Music.id.desc()).all()
    return jsonify(messages=[m.serialize() for m in musics])


@app.route('/music/<id>')
def music_id(id):
    music = Music.query.order_by(Music.id.desc()).get(id)
    if music is None:
        return jsonify(messages="None")
    else:
        return jsonify(messages=music.serialize())


@app.route('/artist')
def artist():
    artists = Artist.query.order_by(Artist.id.desc()).all()
    return jsonify(artist=[m.serialize() for m in artists])


@app.route('/artist/<id>')
def artist_id(id):
    artist = Artist.query.order_by(Artist.id.desc()).get(id)
    if artist is None:
        return jsonify(artist="None")
    else:
        return jsonify(artist=[m.serialize() for m in artist])


@app.route('/')
def home():
    musics = Music.query.order_by(Music.publish_time.desc()).all()
    artist = Artist.query.order_by(Artist.id.desc()).all()
    ret = {
        'music': [m.serialize() for m in musics],
        'artist': [m.serialize() for m in artist]
    }
    return jsonify(ret=ret)
