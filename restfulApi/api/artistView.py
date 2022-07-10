from restfulApi.app import app, db
from restfulApi.model.Artist import Artist
from flask import jsonify, request


@app.route('/artist', methods=['POST', 'GET'])
def artist():
    if request.method == 'POST':
        artistData = Artist(
            name=request.json.get('name'),
            city=request.json.get('city'),
            birth=request.json.get('birth'))
        db.session.add(artistData)
        db.session.commit()
        return jsonify(status="200")
    artists = Artist.query.order_by(Artist.id.desc()).all()
    return jsonify(artist=[m.serialize() for m in artists])


@app.route('/artist/<id>')
def artist_id(id):
    artistData = Artist.query.order_by(Artist.id.desc()).get(id)
    if artist is None:
        return jsonify(artist="None", msg="data is zero")
    else:
        return jsonify(artist=[m.serialize() for m in artistData])
