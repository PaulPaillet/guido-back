import json

from flask import *

import models
import notedetection
from notedetection import *
from models import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test')
def test():
    note = models.Dto(note='do')
    res = json.dumps(note.__dict__)
    return res


@app.route('/oui')
def oui():
    a = notedetection.testFileTObite()
    return json.dumps(a)

@app.route('/process', methods=['POST'])
def process():
    req = request.get_json()
    body = models.Body(**req)
    note = notedetection.processNoteByFile(body)
    return json.dumps(models.Dto(note=note).__dict__)


if __name__ == '__main__':
    app.run(host='192.168.116.209', port=5000, debug=True, threaded=False)
