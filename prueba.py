#!/usr/bin/python
# -*- encoding: utf-8 -*-
import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
import twitter

def oauth_login():
    CONSUMER_KEY = 'FrmCRULEy54WAJyEEzslKBlQf'
    CONSUMER_SECRET = 'TaFwRAtW96yYxfHG54ct4VWyZ3re7tzm8odAJziHlewBsjqGcS'
    OAUTH_TOKEN = '2985454685-oOOuCI4UHUlvmmWok5YToIDRReqwq0epCauRmxC'
    OAUTH_TOKEN_SECRET = 'WIzKDbwqZsKJrxtzI9RwCFAhP7WP85etO4mOZDpL29Aji'

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

def twittear_estado_img(estado):
    twit = oauth_login() 
    status = estado
    with open("uploads/foto.jpg", "rb") as imagefile:
        params = {"media[]": imagefile.read(), "status": status}
        twit.statuses.update_with_media(**params)

def twittear_estado(estado):
    twit = oauth_login() 
    twit.statuses.update(status=estado)

# Initialize the Flask application
app = Flask(__name__)

# Carpeta donde se guarda la imagen temporalmente
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Extensiones admitidas para la imagen
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])

# Comprueba que la extensión es admitida.
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inicio')
def index_inicio():
    return render_template('index.html')

@app.route('/twitterimg')
def index_img():
    return render_template('twitterimg.html')

@app.route('/twittersta')
def index_sta():
    return render_template('twittersta.html')

@app.route('/twitterdrive')
def index_twdrive():
    return render_template('twitterdrive.html')

@app.route('/drive')
def index_drive():
    return render_template('drive.html')

@app.route('/uploadimg', methods=['POST'])
def upload_img():
    file = request.files['file']
    estado = request.form['estado']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'foto.jpg'))
        twittear_estado_img(estado)
        return index()

@app.route('/uploadsta', methods=['POST'])
def upload_sta():
    estado = request.form['estado']
    twittear_estado(estado)
    return index()

@app.route('/uploadtwdrive', methods=['POST'])
def upload_twdrive():
    print("pene")

@app.route('/uploaddrive', methods=['POST'])
def upload_drive():
    print("pene")


if __name__ == "__main__":
    app.run(debug=True)
