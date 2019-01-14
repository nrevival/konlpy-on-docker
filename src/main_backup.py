import json

from bottle import route, run, post, request
from konlpy.tag import Mecab

MECAB = Mecab()

@post('/')
def get_sentence():
    result = dict()
    req = dict(request.json)

    if 'sentences' in req.keys():
        result["sentences"] = req["sentences"]
        result["pos"] = MECAB.pos(req["sentences"])
        result["type"] = "mecab"
        result["result"] = "Success"
    else:
        result["sentences"] = ''
        result["pos"] = []
        result["type"] = "mecab"
        result["result"] = "Fail/문장 전송 실패"    
    return result

run(host='0.0.0.0', 
    port=8899,
    server='gunicorn'
    )
