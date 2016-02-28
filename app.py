import os
import json
from flask import Flask, render_template, \
    request, make_response,\
 url_for, send_from_directory
from werkzeug.wrappers import Response
from werkzeug import secure_filename
import tools.classifier
import pickle

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'csv', 'tsv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.dirname(os.path.realpath(__file__)) + "/uploads"

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            mw = tools.classifier.mentoryWEB(os.path.dirname(os.path.realpath(__file__)) + "/uploads/" + file.filename)
            temp = pickle.dumps(mw)
            
    return render_template('upload.html')

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
