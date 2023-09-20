from flask import Flask
from flask import render_template
from flask import request
from werkzeug.utils import secure_filename

app = Flask(__name__)

#HTML 로드
@app.route('/')
def upload_page():
    return render_template('upload.html')

#파일 업로드
@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'PSOT':
        f = request.files['file']
        f.save('./uploads/' + secure_filename)