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


@app.route('/process', methods=['POST'])
def process():
    req = request.get_json()
    body = models.Body(**req)
    note = notedetection.processNote(body)
    return json.dumps(models.Dto(note="mi").__dict__)


if __name__ == '__main__':
    app.run(host='192.168.26.110', port=5000, debug=True, threaded=False)
