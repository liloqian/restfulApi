from restfulApi.model.Music import Music


def getMusicsName():
    musics = Music.query.order_by(Music.id.desc()).all()
    musicsName = []
    for music in musics:
        musicsName.append(music.name)
    return musicsName
