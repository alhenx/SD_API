#!/usr/bin/python
# -*- encoding: utf-8 -*-

import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
import tweepy
import twitter
import pytumblr

#Autentificación de Tweepy
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

#Twittear estado nuevo junto a imagen
def twittear_estado_img(estado):
    twit = oauth_login() 
    status = estado
    fn = os.path.abspath('uploads/foto.jpg')
    twit.update_with_media(fn, status=status)

#Twittear estado nuevo
def twittear_estado(estado):
    twit = oauth_login() 
    twit.update_status(status=estado)

#Ver los dos últimos twits de un usuario
def ver_estado(nombre,num):
    CONSUMER_KEY = 'FrmCRULEy54WAJyEEzslKBlQf'
    CONSUMER_SECRET = 'TaFwRAtW96yYxfHG54ct4VWyZ3re7tzm8odAJziHlewBsjqGcS'
    ACCESS_KEY = '2985454685-oOOuCI4UHUlvmmWok5YToIDRReqwq0epCauRmxC'
    ACCESS_SECRET = 'WIzKDbwqZsKJrxtzI9RwCFAhP7WP85etO4mOZDpL29Aji'
    auth = twitter.OAuth(ACCESS_KEY, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    t = twitter.Twitter(auth=auth)
    userid = t.users.show(screen_name=nombre)['id']
    datos = t.statuses.user_timeline(user_id=userid, count=num)

    f=open("static/txt/tuits.txt","w")
    for tweet in datos:
        tuit = tweet['text'].encode('utf-8')
        f.write(tuit+'\n') 
    f.close()

    

#Sube una foto a tumblr
def subir_tumblr():
    consumer_key = '6XuUsNVBhpF3I2gkXMTq8jkmoTZYQvp16LsHGCFGBV7X5ObOQW'
    consumer_secret = 'FpChhkP29A8tTxlYgQCCakWwO6Ibx2HX8CmiRj8dyHOFWL5efN'
    token_key = 'FlrqWswNK29GrHAisl5RuE3xRU0tZBHJMmG8r6DUzcWNGS0OxL' 
    token_secret = 'uGKcyOIQ2BrcgFDLsAv6sBrWoesO6ZU63mmR6MTPJXM5tom8qx'

    client = pytumblr.TumblrRestClient(
        consumer_key,
        consumer_secret,
        token_key,
        token_secret
    )
    fn = os.path.abspath('uploads/foto.jpg')
    client.create_photo('sd2015blog', state="published", tags=["SD"], data=fn)


#Inicia flask
app = Flask(__name__)

# Carpeta donde se guarda la imagen temporalmente
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Extensiones admitidas para la imagen
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])

# Comprueba que la extensión es admitida.
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

#Index
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inicio')
def index_inicio():
    return render_template('index.html')

#Página para subir foto a twitter
@app.route('/twitterimg')
def index_img():
    return render_template('twitterimg.html')

#Página para twittear estado
@app.route('/twittersta')
def index_sta():
    return render_template('twittersta.html')

#Página para subir foto a tumblr y twitter
@app.route('/twittertumblr')
def index_twtumblr():
    return render_template('twittertumblr.html')

#Página para subir foto a tumblr
@app.route('/tumblr')
def index_tumblr():
    return render_template('tumblr.html')

#Página para introducir el nombre de quien se desea ver el estado
@app.route('/jsontw')
def index_jsontw():
    return render_template('jsontw.html')

#Página donde se ven los twits
@app.route('/vertw')
def vertw():  
    return render_template("vertw.html")

#Subir foto a twitter y estado
@app.route('/uploadimg', methods=['POST'])
def upload_img():
    file = request.files['file']
    estado = request.form['estado']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'foto.jpg'))
        twittear_estado_img(estado)
        return index()

#Actualizar estado en twitter
@app.route('/uploadsta', methods=['POST'])
def upload_sta():
    estado = request.form['estado']
    twittear_estado(estado)
    return index()

#Ver últimos twits
@app.route('/versta', methods=['POST'])
def ver_sta():
    nombre = request.form['nombre']
    #num = int(request.form['num'])
    ver_estado(nombre,2)
    #return index_jsontw()
    return vertw()

#Subir foto a twitter y tumblr
@app.route('/uploadtwtumblr', methods=['POST'])
def upload_twtumblr():
    file = request.files['file']
    estado = request.form['estado']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'foto.jpg'))
        twittear_estado_img(estado)
        subir_tumblr()
        return index()

#Subir foto a tumblr
@app.route('/uploadtumblr', methods=['POST'])
def upload_tumblr():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'foto.jpg'))
        subir_tumblr()
        return index()


if __name__ == "__main__":
    app.run(debug=True)
