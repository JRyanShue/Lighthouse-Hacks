import json
from flask import Flask
from wtforms import (Form, TextField, validators, SubmitField,
                     DecimalField, IntegerField)
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

import pyrebase

# initialization
config = {
    "apiKey": "AIzaSyDUH2dcnKyDD-_7v6GBlWLGZEPOVGiR8ns",
    "authDomain": "lighthouse-hacks-project.firebaseapp.com",
    "databaseURL": "https://lighthouse-hacks-project-default-rtdb.firebaseio.com",
    "projectId": "lighthouse-hacks-project",
    "storageBucket": "lighthouse-hacks-project.appspot.com",
    "messagingSenderId": "859303759541",
    "appId": "1:859303759541:web:0fe40bf0e010577be738fc",
    "measurementId": "G-SWEXX5VFCS"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

# db.child("names").child("name").push({"name": "ryan"})
db.child("data").child("petitions").update({"name": "Help Zoe"})
users = db.child("data").child("petitions").get()
print(users.val())

app = Flask(__name__)

# @app.route('/login/', methods=['post', 'get'])
# def login():
#     message = ''
#     if request.method == 'POST':
#         review = request.form.get('review')  # access the data inside
#
#         if review:
#             message = "Your review:", review
#         else:
#             message = "No review entered"
#
#     print("pressed")
#
#     return render_template('petitions.html', message=message)

ButtonPressed = 0


@app.route('/sample', methods=["GET", "POST"])
def sample():
    print("yes")
    # return button()
    return render_template("sample.html")


@app.route('/button', methods=["GET", "POST"])
def button():
    # sample()
    return render_template("petitions.html")


def move_forward():
    # Moving forward code
    print("Moving Forward...")


# background process happening without any refreshing
@app.route('/background_process_test')
def add_petition_to_database():
    print("Post a petition")
    return ("nothing")


app.run(host='0.0.0.0', port=5000)
