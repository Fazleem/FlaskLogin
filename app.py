from flask import Flask, render_template, session, redirect
import pymongo
from functools import wraps

app = Flask(__name__)
app.secret_key = b'S\xf1\x98\xc6R\x80\xb8\xbf\xf7\xd3\xec\xea\x16\xb0^\x07'

# Database
client =  pymongo.MongoClient('mongodb+srv://admin:admin@cluster1.mwsmv.mongodb.net/admin?retryWrites=true&w=majority')
db = client.userHandler

#decorators
def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return redirect('/')
  
  return wrap


from user import routes

@app.route('/')
def home():
    return  render_template('home.html')

@app.route('/dashboard/')
@login_required
def dashboard():
    return  render_template('dashboard.html')