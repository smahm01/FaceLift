from flask import Flask, flash, request,render_template, Response, redirect, url_for, session
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import logging
import os
from crop_image import crop_images

app = Flask(__name__, template_folder="client/build", static_folder="client/build/static")

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('HELLO WORLD')

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


@app.route('/url_route', methods=['POST'])
def fileUpload():
    target= "./images" 
    if not os.path.isdir(target):
        os.makedirs(target)
    logger.info("welcome to upload`")
    file = request.files['file_from_react'] 
    filename = secure_filename(file.filename)
    destination="/".join([target, file.filename])
    file.save(destination)
    session['uploadFilePath']=destination
    response={"FileUploaded":"sucess"}
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify', methods=['GET'])
def classify():
    return crop_images()

if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(host='0.0.0.0', port=5001, threaded=True, use_reloader=False)

CORS(app, expose_headers='Authorization')