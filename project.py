from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from band_database_setup import Base, Band, AlbumItem, User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Classic Rock Hall Of Fame"


# Connect to Database and create database session
engine = create_engine('sqlite:///bandalbumswithusers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create anti-forgery state token
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)


@app.route('/fbconnect', methods=['POST'])
def fbconnect():
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = request.data
    print "access token received %s " % access_token

    app_id = json.loads(open('fb_client_secrets.json', 'r').read())['web']['app_id']
    app_secret = json.loads(open('fb_client_secrets.json', 'r').read())['web']['app_secret']
    url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=%s&client_secret=%s&fb_exchange_token=%s' % (app_id, app_secret, access_token)
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]

    # Use token to get user info from API
    userinfo_url = "https://graph.facebook.com/v2.4/me"
    # strip expire tag from access token
    token = result.split("&")[0]


    url = 'https://graph.facebook.com/v2.4/me?%s&fields=name,id,email' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    # print "url sent for API access:%s"% url
    # print "API JSON result: %s" % result
    data = json.loads(result)
    login_session['provider'] = 'facebook'
    login_session['username'] = data["name"]
    login_session['email'] = data["email"]
    login_session['facebook_id'] = data["id"]

    # The token must be stored in the login_session in order to properly logout, let's strip out the information before the equals sign in our token
    stored_token = token.split("=")[1]
    login_session['access_token'] = stored_token

    # Get user picture
    url = 'https://graph.facebook.com/v2.4/me/picture?%s&redirect=0&height=200&width=200' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    data = json.loads(result)

    login_session['picture'] = data["data"]["url"]

    # see if user exists
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    updatePhoto(user_id)

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']

    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '

    flash("Now logged in as %s" % login_session['username'])
    return output


@app.route('/fbdisconnect')
def fbdisconnect():
    facebook_id = login_session['facebook_id']
    # The access token must me included to successfully logout
    access_token = login_session['access_token']
    url = 'https://graph.facebook.com/%s/permissions?access_token=%s' % (facebook_id,access_token)
    h = httplib2.Http()
    result = h.request(url, 'DELETE')[1]
    return "you have been logged out"


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    # ADD PROVIDER TO LOGIN SESSION
    login_session['provider'] = 'google'

    # see if user exists, if it doesn't make a new one
    user_id = getUserID(data["email"])
    if not user_id:
        user_id = createUser(login_session)

    login_session['user_id'] = user_id

    updatePhoto(user_id)

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output

# User Helper Functions

def updatePhoto(user_id):
    thisUser = session.query(User).filter_by(id=user_id).one()
    thisUser.picture = login_session['picture']
    session.add(thisUser)
    session.commit()

def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session['email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None

# DISCONNECT - Revoke a current user's token and reset their login_session


@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    credentials = login_session.get('credentials')
    if credentials is None:
        response = make_response(json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = credentials.access_token
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] != '200':
        # For whatever reason, the given token was invalid.
        response = make_response(
            json.dumps('Failed to revoke token for given user.'), 400)
        response.headers['Content-Type'] = 'application/json'
        return response


# JSON APIs to view Band and Album Information
@app.route('/band/<int:band_id>/albums/JSON')
def bandAlbumsJSON(band_id):
    band = session.query(Band).filter_by(id=band_id).one()
    albums = session.query(AlbumItem).filter_by(band_id=band_id).all()
    return jsonify(AlbumItems=[i.serialize for i in albums])


@app.route('/album/<int:album_id>/JSON')
def albumItemJSON(album_id):
    Album_Item = session.query(AlbumItem).filter_by(id=album_id).one()
    return jsonify(Album_Item=Album_Item.serialize)

@app.route('/albums/JSON')
def albumsJSON():
    albums = session.query(AlbumItem).all()
    return jsonify(albums=[r.serialize for r in albums])

@app.route('/bands/JSON')
def bandsJSON():
    bands = session.query(Band).all()
    return jsonify(bands=[r.serialize for r in bands])


# Show all restaurants
@app.route('/')
@app.route('/bands/')
def showBands():
    bands = session.query(Band).order_by(asc(Band.name))
    if 'username' not in login_session:
        return render_template('publicbands.html', bands=bands)
    else:
        return render_template('bands.html', bands=bands)

# Create a new band


@app.route('/band/new/', methods=['GET', 'POST'])
def newBand():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newBand = Band(name=request.form['name'], picture=request.form['picture'], description=request.form['description'], user_id=login_session['user_id'])
        session.add(newBand)
        flash('New Band %s Successfully Created' % newBand.name)
        session.commit()
        return redirect(url_for('showBands'))
    else:
        return render_template('newBand.html')

# Edit a band


@app.route('/band/<int:band_id>/edit/', methods=['GET', 'POST'])
def editBand(band_id):
    editedBand = session.query(Band).filter_by(id=band_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if editedBand.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not authorized to edit this band. Please create your own band in order to edit.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        if request.form['name']:
            editedBand.name = request.form['name']
            editedBand.picture = request.form['picture']
            editedBand.description = request.form['description']
            session.add(editedBand)
            session.commit()
            flash('Band Successfully Edited %s' % editedBand.name)
            return redirect(url_for('showAlbums', band_id=band_id))
    else:
        return render_template('editBand.html', band=editedBand)


# Delete a band
@app.route('/band/<int:band_id>/delete/', methods=['GET', 'POST'])
def deleteBand(band_id):
    bandToDelete = session.query(Band).filter_by(id=band_id).one()
    albumsToDelete = session.query(AlbumItem).filter_by(band_id=band_id).all()
    if 'username' not in login_session:
        return redirect('/login')
    if bandToDelete.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not authorized to delete this band. Please create your own band in order to delete.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        session.delete(bandToDelete)
        if albumsToDelete !=[]:
            for i in albumsToDelete:
                session.delete(i)
        flash('%s Successfully Deleted' % bandToDelete.name)
        session.commit()
        return redirect(url_for('showBands', band_id=band_id))
    else:
        return render_template('deleteband.html', band=bandToDelete)

# Show albums for a band

@app.route('/band/<int:band_id>/')
@app.route('/band/<int:band_id>/albums/')
def showAlbums(band_id):
    band = session.query(Band).filter_by(id=band_id).one()
    creator = getUserInfo(band.user_id)
    albums = session.query(AlbumItem).filter_by(band_id=band_id).all()
    if 'username' not in login_session or creator.id != login_session['user_id']:
        return render_template('publicalbums.html', albums=albums, band=band, creator=creator)
    else:
        return render_template('albums.html', albums=albums, band=band, creator=creator)


# Create a new album
@app.route('/band/<int:band_id>/album/new/', methods=['GET', 'POST'])
def newAlbum(band_id):
    if 'username' not in login_session:
        return redirect('/login')
    band = session.query(Band).filter_by(id=band_id).one()
    if login_session['user_id'] != band.user_id:
        return "<script>function myFunction() {alert('You are not authorized to add albums  to this band. Please create your own band in order to add albums.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        newItem = AlbumItem(name=request.form['name'], description=request.form['description'], year=request.form['year'], picture=request.form['picture'], price=request.form['price'], era=request.form['course'], band_id=band_id, user_id=band.user_id)
        session.add(newItem)
        session.commit()
        flash('New Album %s Successfully Created' % (newItem.name))
        return redirect(url_for('showAlbums', band_id=band_id))
    else:
        return render_template('newalbumitem.html', band_id=band_id)

# Edit an album


@app.route('/band/<int:band_id>/album/<int:album_id>/edit', methods=['GET', 'POST'])
def editAlbumItem(band_id, album_id): # start here, rick
    if 'username' not in login_session:
        return redirect('/login')
    editedAlbum = session.query(AlbumItem).filter_by(id=album_id).one()
    band = session.query(Band).filter_by(id=band_id).one()
    if login_session['user_id'] != band.user_id:
        return "<script>function myFunction() {alert('You are not authorized to edit albums of this band. Please create your own band in order to edit albums.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        if request.form['name']:
            editedAlbum.name = request.form['name']
        if request.form['year']:
            editedAlbum.year = request.form['year']
        if request.form['description']:
            editedAlbum.description = request.form['description']
        if request.form['picture']:
            editedAlbum.picture = request.form['picture']
        if request.form['price']:
            editedAlbum.price = request.form['price']
        if request.form['era']:
            editedAlbum.era = request.form['era']
        session.add(editedAlbum)
        session.commit()
        flash('Album Successfully Edited')
        return redirect(url_for('showAlbums', band_id=band_id))
    else:
        return render_template('editalbumitem.html', band_id=band_id, album_id=album_id, item=editedAlbum)


# Delete an album
@app.route('/band/<int:band_id>/album/<int:album_id>/delete', methods=['GET', 'POST'])
def deleteAlbumItem(band_id, album_id):
    if 'username' not in login_session:
        return redirect('/login')
    band = session.query(Band).filter_by(id=band_id).one()
    AlbumToDelete = session.query(AlbumItem).filter_by(id=album_id).one()
    if login_session['user_id'] != band.user_id:
        return "<script>function myFunction() {alert('You are not authorized to delete albums from this band. Please create your own band in order to delete albums.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        session.delete(AlbumToDelete)
        session.commit()
        flash('Album Successfully Deleted')
        return redirect(url_for('showAlbums', band_id=band_id))
    else:
        return render_template('deletealbumitem.html', item=AlbumToDelete)


# Disconnect based on provider
@app.route('/disconnect')
def disconnect():
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            gdisconnect()
            del login_session['gplus_id']
            del login_session['access_token']
        if login_session['provider'] == 'facebook':
            fbdisconnect()
            del login_session['facebook_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']
        del login_session['provider']
        flash("You have successfully been logged out.")
        return redirect(url_for('showBands'))
    else:
        flash("You were not logged in")
        return redirect(url_for('showBands'))


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
