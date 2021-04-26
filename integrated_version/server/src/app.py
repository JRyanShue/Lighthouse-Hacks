import json
from flask import Flask
from wtforms import (Form, TextField, validators, SubmitField,
                     DecimalField, IntegerField)
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

import time

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
# db.child("data").child("petitions").update({"name": "Help Zoe"})
# users = db.child("data").child("petitions").get()
# print(users.val())

# db.child("data").child("announcements").update({"name": "Help Zoe"})
# db.child("data").child("clubs").update({"name": "Help Zoe"})
# db.child("data").child("surveys").update({"name": "Help Zoe"})

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


@app.route('/petition_form', methods=["GET", "POST"])
def petition_form():
    print("yes")
    message = ''
    if request.method == 'POST':
        name = request.form.get('name')  # access data from form
        author = request.form.get('author')
        link = request.form.get('link')
        content = request.form.get('content')
        timestamp = time.ctime(time.time())

        if name and author and link and content:
            # push to firebase
            db.child("data").child("petitions").push(
                {"Timestamp": timestamp, "Petition": name, "Author": author, "Link": link, "Content": content})

            message = "Success"
        else:
            if not name:
                message += "Please enter a petition name."
            if not author:
                message += "\nPlease enter an author name."
            if not link:
                message += "\nPlease enter a link to your petition."
            if not content:
                message += "\nPlease enter a petition description."

        print("yessir")
        print("name:", name)
        print("author:", author)
        print("link:", link)
        print("content:", content)
        print(message)
    # return button()
    return render_template("petition_form.html", message=message)


@app.route('/announcements_form', methods=["GET", "POST"])
def announcements_form():
    print("yes1")
    message = ''
    if request.method == 'POST':
        name = request.form.get('name')  # access data from form
        author = request.form.get('author')
        details = request.form.get('details')
        timestamp = time.ctime(time.time())

        if name and author and details:
            # push to firebase
            db.child("data").child("announcements").push(
                {"Timestamp": timestamp, "Announcement": name, "Author": author, "Details": details})

            message = "Success"
        else:
            if not name:
                message += "Please enter an announcement."
            if not author:
                message += "\nPlease enter an author name."
            if not details:
                message += "\nPlease enter announcement details."

        print("announcement")
    # return button()
    return render_template("announcements_form.html", message=message)


@app.route('/clubs_form', methods=["GET", "POST"])
def clubs_form():
    print("yes2")
    message = ''
    if request.method == 'POST':
        name = request.form.get('name')  # access data from form
        author = request.form.get('author')
        details = request.form.get('details')
        timestamp = time.ctime(time.time())

        if name and author and details:
            # push to firebase
            db.child("data").child("clubs").push(
                {"Timestamp": timestamp, "Club Announcement": name, "Author": author, "Details": details})

            message = "Success"
        else:
            if not name:
                message += "Please enter a club announcement."
            if not author:
                message += "\nPlease enter an author name."
            if not details:
                message += "\nPlease enter announcement details."

        print("club")
    # return button()
    return render_template("clubs_form.html", message=message)


@app.route('/surveys_form', methods=["GET", "POST"])
def surveys_form():
    print("yes3")
    message = ''
    if request.method == 'POST':
        name = request.form.get('name')  # access data from form
        author = request.form.get('author')
        details = request.form.get('details')
        link = request.form.get('link')
        timestamp = time.ctime(time.time())

        if name and author and details and link:
            # push to firebase
            db.child("data").child("surveys").push(
                {"Timestamp": timestamp, "Survey": name, "Link": link, "Author": author, "Details": details})

            message = "Success"
        else:
            if not name:
                message += "Please enter a survey name."
            if not author:
                message += "\nPlease enter an author name."
            if not details:
                message += "\nPlease enter survey details."
            if not link:
                message += "\nPlease enter a link to your survey."

        print("survey")
    # return button()
    return render_template("surveys_form.html", message=message)


@app.route('/home', methods=["GET", "POST"])
def home():
    # sample()
    all_petitions = db.child("data").child("petitions").get()
    petitions = all_petitions.val()
    print(petitions.values())
    return render_template("petitions.html", data=petitions.values())  # pass JSON of petition data to the HTML page


def move_forward():
    # Moving forward code
    print("Moving Forward...")


# background process happening without any refreshing
@app.route('/background_process_test')
def add_petition_to_database():
    print("Post a petition")
    return ("nothing")


@app.route('/test')
def test():
    # print("Post a petition")
    return render_template("main_page.html")


@app.route('/announcements')
def announcements():
    announcements_all = db.child("data").child("announcements").get()
    announcements_data = announcements_all.val()
    return render_template("Announcements.html", data=announcements_data.values())


@app.route('/clubs')
def clubs():
    all_clubs = db.child("data").child("clubs").get()
    clubs_data = all_clubs.val()
    return render_template("Clubs.html", data=clubs_data.values())


@app.route('/petitionspage')
def petitionspage():
    all_petitions = db.child("data").child("petitions").get()
    petitions = all_petitions.val()
    return render_template("PetitionsPage.html", data=petitions.values())  # pass petition data to the HTML page django


@app.route('/surveys')
def surveys():
    all_surveys = db.child("data").child("surveys").get()
    surveys_data = all_surveys.val()
    return render_template("Surveys.html", data=surveys_data.values())


@app.route('/sign_in')
def sign_in():
    return render_template("SignInPage.html")


app.run(host='0.0.0.0', port=5000)
