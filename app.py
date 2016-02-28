import json
from flask import Flask, render_template, \
    request, make_response
from werkzeug.wrappers import Response

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        data = json.loads(request.data.decode())
        odata = json.dumps(data)
        return Response(odata, mimetype='text/json')

if __name__ == '__main__':
    app.debug = True
    app.run()
