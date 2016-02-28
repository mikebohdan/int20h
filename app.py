import os
import json
from flask import Flask, render_template, \
    request, make_response,\
 url_for, send_from_directory
from werkzeug.wrappers import Response
from werkzeug import secure_filename
from flask.ext.sqlalchemy import SQLAlchemy
import tools.classifier
import pickle

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'csv', 'tsv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.dirname(os.path.realpath(__file__)) + "/uploads"
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

class Example(db.Model):
    __tablename__ = "examples"
    a = db.Column(db.LargeBinary(), primary_key=True)

try:
    db.create_all()
except Exception:
    pass

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            mw = tools.classifier.mentoryWEB(os.path.dirname(os.path.realpath(__file__)) + "/uploads/" + file.filename)
            db.session.add(Exception(a=pickle.dumps(mw)))
            return
    else:
        print(get_url)
        return render_template('upload.html')

@app.route('/api/<id>', methods=['POST'])
def api(id):
    pass

if __name__ == '__main__':
    app.debug = True
    app.run()
