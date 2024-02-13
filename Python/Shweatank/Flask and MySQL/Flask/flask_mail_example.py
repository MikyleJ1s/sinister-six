from flask import * 
from flask_mail import *
import mysql.connector

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'policy.management.system.email@gmail.com' #myemail
app.config['MAIL_PASSWORD'] = 'admin_password' #mypassword
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route("/")
def index():
    msg = Message('subject', sender = 'policy.management.system.email@gmail.com', recipients=['3830197@myuwc.ac.za'])
    msg.body = 'hi, this is the email sent by using the flask web application'
    return "Mail Sent, Please Check the Mail ID"

@app.route("/savedetails", methods = ["GET","POST"])
def savedetails():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]
            address = request.form["address"]
            with mysql.connector.connect("policy_management_system") as con:
                cur = con.cursor()
                cur.execute("insert into users (username, password) values (?,?)", (name,email))
                con.commit()    
                msg = "Employee successfully added"
        except:
            con.rollback()
            msg = "Cannot add employee"
        finally:
            return render_template("home")

if __name__ == "__main__":
    app.run(debug=True)
