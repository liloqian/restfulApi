from restfulApi.app import app, db
from restfulApi.model.Music import Music
from flask import jsonify, request
from datetime import datetime


@app.route('/music', methods=['POST', 'GET'])
def music():
    if request.method == 'POST':
        musicData = Music(
            name=request.json.get('name'),
            author=request.json.get('author'),
            publish_time=datetime.now())
        db.session.add(musicData)
        db.session.commit()
        return jsonify(status="200")
    musics = Music.query.order_by(Music.id.desc()).all()
    return jsonify(messages=[m.serialize() for m in musics])


@app.route('/music/<id>')
def music_id(id):
    musicData = Music.query.order_by(Music.id.desc()).get(id)
    if music is None:
        return jsonify(messages="None")
    else:
        return jsonify(messages=musicData.serialize())
