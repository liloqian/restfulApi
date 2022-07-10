import time
from restfulApi.app import app
from flask import jsonify, request


filePath = '/static/file/'


@app.route('/uploadPic', methods=['POST', 'GET'])
def uploadPic():
    picFile = request.files.get("pic")
    fileName, fileExt = picFile.filename.split('.')
    newFileName = fileName + '_' + time.time().__str__() + '.' + fileExt
    newPath = app.root_path + filePath + newFileName
    picFile.save(newPath)
    retPath = request.host_url + filePath + newFileName
    return jsonify({"msg": "upload success", "path": retPath})
