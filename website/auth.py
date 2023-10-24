from flask import Blueprint,render_template, request
import csv


auth = Blueprint('auth',__name__)

@auth.route('/', methods = ['GET','POST'])
def login():
    msg = ''
    happy = ''
    if request.method == 'POST':
        email = request.form.get('email')
        passw = request.form.get('pass')
        remember = request.form.get('rememberr')
        
        if '@' not in email.lower():
            msg = "Invalid Email"
        elif '.com' not in email.lower():
            msg = "Invalid Email"
        elif len(passw)<8:
            msg = "Invalid Password"
        else:
            with open('accounts.csv', mode='r') as file:
                reader = csv.reader(file)
                file.seek(0)
                data = [email.lower(),passw]
                for row in reader:
                    if data[0] == row[0] and data[1] == row[2]:
                        print("Success")
                        happy = "Login Successful"
                        msg = ''
                        return render_template("home.html")
                    else:
                        msg = "Invalid Login Info"          
    return render_template("login.html", message = msg, success = happy)

@auth.route('/registration', methods = ['GET','POST'])
def registration():
    msg = ''
    happy = ''
    if request.method == 'POST':
        email = request.form.get('email')
        enroll = request.form.get('enroll')
        passw = request.form.get('pass')
        conpass = request.form.get('conpass')
        
        
        if '@' not in email.lower():
            msg = "Invalid Email"
        elif '.com' not in email.lower():
            msg = "Invalid Email"
        elif len(passw)<8:
            msg = "Password must be at least 8 characters long"
        elif passw!=conpass:
            msg = "Passwords doesn't match"
        elif enroll != '' and 'mitu' not in enroll.lower():
            msg = "Invalid Enrollment Number"
        else:
            with open('accounts.csv', mode='a+', newline='') as file:
                writer = csv.writer(file)
                reader = csv.reader(file)
                data = [email.lower(),enroll.lower()]
                count = 0
                file.seek(0)
                for row in reader:
                    if data[0] == row[0]:
                        msg = "Email is already Registered"
                        count = 1
                        break
                    else:
                        pass
                if count == 0:
                    writer.writerow([email.lower(), enroll.lower(), passw])
                    print("Registered")
                    msg = ''
                    happy = "Registered Successfully" 
    return render_template("registration.html",message = msg, success = happy)



