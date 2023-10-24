from flask import Blueprint,render_template

views = Blueprint('views',__name__)

@views.route('/home')
def home():
    return render_template("home.html")

@views.route('/announcements')
def announcements():
    return render_template("announcements.html")

@views.route('/communities')
def communities():
    return render_template("communities.html")

@views.route('/help', methods = ['GET','POST'])
def help():
    return render_template("help.html")

@views.route('/profile', methods = ['GET','POST'])
def profile():
    return render_template("profile.html")
