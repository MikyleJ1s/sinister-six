import json
from flask import Flask, redirect, render_template, url_for, request

app = Flask(__name__)
x = 10
y = 15

@app.route("/home")
def home():
    return "Hello World, this is the Home Page"

@app.route("/info/<name>")
def info(name):
    return str(name)+" has "+str(len(name))+" characters!"

@app.route("/calculate/<int:xvalue>/<operator>/<int:yvalue>")
def calculate(xvalue, operator,yvalue):
    if operator == "add":
        return str(xvalue)+"+"+str(yvalue)+"="+str(xvalue+yvalue)
    elif operator == "sub":
        return str(xvalue)+"-"+str(yvalue)+"="+str(xvalue-yvalue)
    elif operator == "mul":
        return str(xvalue)+"*"+str(yvalue)+"="+str(xvalue*yvalue)
    elif operator == "div":
        if yvalue == 0:
            return str(xvalue)+"/"+str(yvalue)+"=Impossible"
        return str(xvalue)+"/"+str(yvalue)+"="+str(xvalue/yvalue)

@app.route("/admin")
def greet_admin():
    return "Hello Admin"

@app.route("/guest/<guest>")
def greet_guest(guest):
    return "Hello " +guest

@app.route("/user/<name>")
def greet_user(name):
    if name == "admin":
        return redirect(url_for("greet_admin"))
    else:
        return redirect(url_for("greet_guest", guest = name))

@app.route('/login', methods=['GET', 'POST'])
def user_login():
    with open("credentials.json", 'r') as f:
        creds = json.load(f)
        
    error = ""
    if request.method == 'POST':
        if request.form['username'] in creds['usernames'] and request.form['password'] in creds['passwords'] and list(creds.values())[0].index(request.form['username']) == list(creds.values())[1].index(request.form['password']):
             return render_template('login.html', error='Successful Login.')
        else:
             return render_template('login.html', error='Invalid Credentials.')
    return render_template('login.html', error=error)

@app.route("/")
def index():
    return render_template('flaskhtml.html')

@app.route("/success/<name>")
def success(name):
    return "Welcome " +name

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form['nm']
        return redirect(url_for("success", name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for("success", name = user))



@app.route("/add")
def add():
    return str(x)+"+"+str(y)+"="+str(x+y)

@app.route("/sub")
def sub():
    return str(x)+"-"+str(y)+"="+str(x-y)

@app.route("/mul")
def mul():
    return str(x)+"*"+str(y)+"="+str(x*y)

@app.route("/div")
def div():
    if y == 0:
        return str(x)+"/"+str(y)+" is not possible"
    return str(x)+"/"+str(y)+"="+str(round(x/y,2))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
    #app.run()
