from flask import Blueprint,render_template, request



import csv
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

@views.route('/academics')
def academics():
    return render_template("academics.html")

@views.route('/maps')
def maps():
    return render_template("maps.html")

@views.route('/help', methods = ['GET','POST'])
def help():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        message = request.form.get('message')
        with open('questions.csv', mode='a+', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name,phone, email, message])
    return render_template("help.html")

@views.route('/profile', methods = ['GET','POST'])
def profile():
    from .auth import token
    name = ''
    enroll = ''
    email = ''
    course = ''

    with open('details.csv', mode='r') as file:
        reader = csv.reader(file)
        file.seek(0)
        for row in reader:
            if token == row[2]:
                email = row[0]
                enroll = row[1]
                name = row[3]
                course = row[4]

                
                
    return render_template("profile.html", name = name, enroll = enroll.upper(), email = email, course = course.upper() )
