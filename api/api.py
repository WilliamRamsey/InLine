from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
import re
from person import *


def get_page(location):
    file = open(location, "r")
    page = file.read()
    file.close()
    return page

app = Flask(__name__)


# Flow for adding user to line
# QR code routes to

@app.route('/')
def route_to_new_person():
    return redirect("/new_person.html", code=302)

@app.route('/new_person.html')
def new_person():
    page = get_page("client/new_person.html")
    return page

# Adds person to line
@app.route("/create_new_person.py", methods=['POST', 'GET'])
def create_new_person():
    phone = request.args.get("phone_num")
    phone = str(re.sub(r'\D', '', phone))
    carrier = request.args.get("carrier")

    new_user = Person(phone=phone, carrier=carrier)
    new_user.add_to_line()
    return redirect(f"/display_person.html?id={new_user.id}", code=302)


@app.route('/display_person.html')
# returns order in line
def display_person():
    user = Person(id=int(request.args.get("id")))
    page = get_page("C:/Users/willi/OneDrive/Desktop/In_Line/client/display_person.html")
    page = page.format(id=str(user.id))
    return page


# Flow for moving the next person into line
#
@app.route('/move_line.html')
def move_line():
    page = get_page('C:/Users/willi/OneDrive/Desktop/In_Line/client/move_line.html')
    return page

# Backend endpoints for htmx to access
#
#
"""
@app.route('/person/phone')
def get_phone():
    user = Person(id=int(request.args.get("id")))
    user.link_to_database()
    return user.phone
"""
    
@app.route('/person/phone')
def get_phone():
    user = Person(id=int(request.args.get("id")))
    return user.phone

@app.route('/person/place')
def get_place():
    user = Person(id=int(request.args.get("id")))
    return str(user.calculate_place())


@app.route('/next_person')
def next_person():
    pass

# Utilities (javascript and css files)
@app.route('/utils/javascript/refresh_page.js')
def refresh_page():
    js = get_page("C:/Users/willi/OneDrive/Desktop/In_Line/client/scripts/refresh_page.js")
    return js

app.run(port=5500, debug=True)
