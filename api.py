#!/usr/bin/python
# -*- encoding: utf-8 -*-

import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
import tweepy
import twitter
import time


def oauth_login():
    CONSUMER_KEY = 'FrmCRULEy54WAJyEEzslKBlQf'
    CONSUMER_SECRET = 'TaFwRAtW96yYxfHG54ct4VWyZ3re7tzm8odAJziHlewBsjqGcS'
    ACCESS_KEY = '2985454685-oOOuCI4UHUlvmmWok5YToIDRReqwq0epCauRmxC'
    ACCESS_SECRET = 'WIzKDbwqZsKJrxtzI9RwCFAhP7WP85etO4mOZDpL29Aji'

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    auth2 = twitter.OAuth(ACCESS_KEY, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)


    twit = tweepy.API(auth)
    return twit

def twittear_estado_img(estado):
    twit = oauth_login() 
    status = estado
    fn = os.path.abspath('uploads/foto.jpg')
    twit.update_with_media(fn, status=status)

def twittear_estado(estado):
    twit = oauth_login() 
    twit.update_status(status=estado)

def ver_estado(nombre,num):
    CONSUMER_KEY = 'FrmCRULEy54WAJyEEzslKBlQf'
    CONSUMER_SECRET = 'TaFwRAtW96yYxfHG54ct4VWyZ3re7tzm8odAJziHlewBsjqGcS'
    ACCESS_KEY = '2985454685-oOOuCI4UHUlvmmWok5YToIDRReqwq0epCauRmxC'
    ACCESS_SECRET = 'WIzKDbwqZsKJrxtzI9RwCFAhP7WP85etO4mOZDpL29Aji'
    auth = twitter.OAuth(ACCESS_KEY, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    t = twitter.Twitter(auth=auth)
    userid = t.users.show(screen_name=nombre)['id'] #Consigue la id del usuario que elegimos
    datos = t.statuses.user_timeline(user_id=userid, count=num) #Escoge los tweets del usuario elegido y la cantidad de tweets

    f=open("static/txt/tuits.txt","w")
    for tweet in datos:
        tuit = tweet['text'].encode('utf-8')
        f.write(tuit+'\n') 
    f.close()

'''
#TWITTER + DRIVE
def twitter_drive():

#DRIVE
def subir_drive():


'''

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

@app.route('/jsontw')
def index_jsontw():
    return render_template('jsontw.html')

@app.route('/vertw')
def vertw():  
    return render_template("vertw.html")

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

@app.route('/versta', methods=['POST'])
def ver_sta():
    nombre = request.form['nombre']
    #num = int(request.form['num'])
    ver_estado(nombre,2)
    #return index_jsontw()
    return vertw()
'''
#TWITTER + DRIVE
@app.route('/uploadtwdrive', methods=['POST'])
def upload_twdrive():
    twittear_drive();
    return index()

#DRIVE
@app.route('/uploaddrive', methods=['POST'])
def upload_drive():
    subir_drive();
    return index()
'''

if __name__ == "__main__":
    app.run(debug=True)
