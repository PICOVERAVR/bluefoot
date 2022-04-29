# Before running, set env variables:
# export FLASK_APP=UI.py
# export FLASK_DEBUG=1 for true, 0 for false
# [Navigate to bluefoot/src/UI_Integrations]
# flask run

# Now you can pull up localhost:5000 in your browser to view the webpage. Refresh to see changes.

# Note: DO NOT SET DEBUG MODE IF DEPLOYING PUBLICLY!!! ---------------------------------------------------
#   Debug mode allows for arbitrary code executions from the deployed site. log4j flashbacks...

# Disclaimer: A majority of this boilerplate was written alongside the YouTube tutorials by Corey Schafer

from flask import Flask, render_template, url_for, flash, request,redirect
from forms import registerform,Loginform
from turbo_flask import Turbo
from datetime import datetime, timedelta
from time import sleep
import threading
from Oauth import Oauth
import newthing

app = Flask(__name__)

# WHEN DEPLOYING PUBLICLY, GENERATE A NEW ONE AND MAKE IT AN ENVIRONMENT VARIABLE OR SOMETHING INSTEAD,
#   OTHERWISE THIS KEY IS USELESS FOR PREVENTING SECURITY RISKS
app.config['SECRET_KEY'] = '1c54243c5e2a20c2fbcccee5f28ff349'
turbo = Turbo(app)

def test_url(self):
    with app.app_context(), app.test_request_context():
        self.assertEqual('/', url_for('root.home'))

test_data = [
    {
        'id': 0,
        'content': 'N/A'
    },
    {
        'id': 1,
        'content': 'data 1'
    }
]

# Home page route
@app.route("/")
@app.route("/home")
@app.route("/index.html")
def home():
    return render_template("home.html")

# smol page route
@app.route("/smol", methods=['POST', 'GET'])
def smol():
    if request.method == 'POST':
        if request.form['On-Off Button'] == 'on':
            print("smol: On button pressed")
            test_data[0]['content'] = 'ON'
            turbo.push(turbo.replace(render_template('smol_button_status.html'), 'button_status'))
        elif request.form['On-Off Button'] == 'off':
            print("smol: Off button pressed")
            test_data[0]['content'] = 'OFF'
            turbo.push(turbo.replace(render_template('smol_button_status.html'), 'button_status'))
    
    return render_template("smol.html", title='smol')



# Chungus page route
@app.route("/chungus")
def chungus():
    return render_template("chungus.html", title='Chungus')
#login page route
@app.route("/login",methods = ['GET','POST'])
def Login():
    form = Loginform()
    if form.validate_on_submit():
        if form.username.data == "admin" and form.password.data == "admin":
            flash('you have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('login unsuccessful. please check username and password','danger')

    return render_template("login.html", title='login',form = form)

@app.route("/register",methods = ['GET','POST'])
def Register():
    form = registerform()
    if form.validate_on_submit():
        flash(f'Account has been created for {form.username.data}!','successful')
        return redirect(redirect(url_for('home')))
    #return render_template("register.html", title='Register',form = form)
    return redirect(Oauth.discordloginurl)

@app.route("/discord",methods = ['GET','POST'])
def discord():
    code = request.args.get("code")
    #access_token = Oauth.get_discord_token(code)
    access_token  = newthing.Oauth.get_discord_token(code)
    #print("the access token was ",access_token)
    newuser = newthing.Oauth.get_current_user(access_token['access_token'])
    user = newuser.get("username")
   # print("the user token was ",user)
    newthing.Oauth.get_message(928457965890056242)
    return access_token

# Set global data (be careful... this is necessary for avoiding javascript,
#   but global variables can be dangerous/messy)
@app.context_processor
def inject_data():
    dynamic_vars = {}

    # For Spotify, retrieve data and format it something like this:
    # spotify_API_retrieve = Spotify.retrieve() ... blablabla
    spotify_data = [
        {
        'title': 'Never Gonna Give You Up',
        'artist': 'Rick Astley',
        'album': 'Whenever You Need Somebody',
        'time_elapsed': str(timedelta(seconds=72)), # Replace 72 with spotify_API_retrieve.song_length or whatever
        'length': str(timedelta(seconds=212)), # Replace 212 with however many seconds long the song is
        }
]

    # Add dictionaries entries for dynamic data here
    dynamic_vars['chungus_current_time'] = datetime.now().strftime("%H:%M:%S")
    dynamic_vars['spotify_data'] = spotify_data
    dynamic_vars['test_data'] = test_data

    return dynamic_vars

# Visually update chungus's display 1. Call from separate
#   thread in before_first_request(), as this runs in an infinite loop.
def update_chungus_d1():
    with app.app_context():
        while True:
            sleep(1)
            turbo.push(turbo.replace(render_template('chungus_display_1.html'), 'display-1')) # look into the "to" argument for client-specific updates



@app.before_first_request
def before_first_request():
    threading.Thread(target=update_chungus_d1).start()



# if __name__ == '__main__':
#     app.run(debug=True)