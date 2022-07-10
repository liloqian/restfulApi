from restfulApi.app import app, db
from restfulApi.api import musicView, helloView, artistView
from flask import request
from restfulApi.command.command import *


if __name__ == '__main__':
    app.run()


@app.before_request
def before_request():
    # print("method: %s, header: %s" % (request.method, request.headers.environ))
    printRequest('before_request')


@app.before_first_request
def before_first_request():
    printRequest('before_first_request')


def printRequest(tag):
    print("%s method: %s, url: %s, cookie: %s, values: %s, data: %s" % (tag, request.method, request.url,
                                                                        request.cookies, request.values, request.data))
