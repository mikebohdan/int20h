import json
from flask import render_template
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        for i in request.__dict__:
            print("{} -> {}".format(i, getattr(request, i)))
        return json.dumps({'name': 'LOL'})

if __name__ == '__main__':
    app.debug = True
    app.run()
