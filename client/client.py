from restfulApi.model.Music import Music
from restfulApi.model.Artist import Artist
from faker import Faker
import requests
import json

fake = Faker(locale='zh_CN')


def getIndex():
    res = requests.get("http://127.0.0.1:5000/")
    res.encoding = "utf-8"
    printResponse(res)


def getMusics(id=None):
    url = 'http://127.0.0.1:5000/music/'
    if id is not None:
        url += id.__str__()
    res = requests.get(url)
    res.encoding = "utf-8"
    printResponse(res)


def postMusic():
    music = Music(
        name=fake.sentence(),
        author=fake.name(),
        publish_time=fake.date_time_this_year())
    headers = {'CONTENT_TYPE': 'application/json'}
    res = requests.post("http://127.0.0.1:5000/music", data=json.dumps(music.serialize()), headers=headers)
    printResponse(res)


def getArtists():
    res = requests.get("http://127.0.0.1:5000/artist")
    res.encoding = "utf-8"
    printResponse(res)


def postArtist():
    artist = Artist(
        name=fake.name(),
        birth=fake.date_time_this_year(),
        city=fake.city()
    )
    headers = {'CONTENT_TYPE': 'application/json'}
    res = requests.post("http://127.0.0.1:5000/music", data=json.dumps(artist.serialize()), headers=headers)
    printResponse(res)


def printResponse(response):
    dict = {}
    dict['url'] = response.request.url
    dict['method'] = response.request.method
    if response.request.body is None:
        dict['reqData'] = ""
    else:
        dict['reqData'] = response.request.body.encode('utf-8').decode("unicode_escape")
    dict['code'] = response.status_code
    dict['resText'] = response.content.decode("unicode_escape")
    # dict['resJson'] = response.json
    # dict['resHeader'] = response.headers
    print(dict)


if __name__ == '__main__':
    getIndex()
    postMusic()
    getMusics(11)
    postArtist()
    getArtists()
