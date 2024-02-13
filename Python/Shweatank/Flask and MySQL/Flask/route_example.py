from flask import *
import json, mysql.connector

app = Flask(__name__)
myconn = mysql.connector.connect(host="localhost", user="root", passwd="Mikyle123", database="policy_management_system")
cur = myconn.cursor()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/validate", methods = ["POST"])
def validate():
    if request.method == "POST" and request.form['password'] == "pass":
        return redirect(url_for("success"))
    else:
        abort(401) 
    #return redirect(url_for("login"))

@app.route('/login-1', methods=['GET', 'POST'])
def json_login():
    with open("Shweatank/Flask and MySQL/credentials.json", 'r') as f:
        creds = json.load(f)

    if request.method == 'POST':
        if request.form['username'] in creds['usernames'] and request.form['password'] in creds['passwords'] and list(creds.values())[0].index(request.form['username']) == list(creds.values())[1].index(request.form['password']):
             return redirect('success')
        else:
             return render_template('login.html')
    return render_template('login.html')

@app.route('/login-2', methods=['GET', 'POST'])
def database_login():
    try:
             
        if request.method == 'POST':
            query = "select * from users where username = '" + request.form['username'] + "' and password = '" + request.form['password'] + "'"
            cur.execute(query)
            useraccount = cur.fetchone()
            
            if useraccount:
                return redirect(url_for('success'))
            else: 
                return render_template('login.html')
                
        elif request.method == 'GET':
            return render_template('login.html')
        return render_template('login.html')
    
    except:
        myconn.rollback()
    myconn.close()

@app.route('/login-3', methods=['GET', 'POST'])
def dictionary_login():
    creds = {
    "usernames": ["bob@gmail.com", "tom@gmail.com", "meg@gmail.com"], 
    "passwords": ["bob", "tom", "meg"]
    }

    if request.method == 'POST':
        if request.form['username'] in creds['usernames'] and request.form['password'] in creds['passwords'] and list(creds.values())[0].index(request.form['username']) == list(creds.values())[1].index(request.form['password']):
             return redirect('success')
        else:
             return render_template('login.html')
    return render_template('login.html')

@app.route('/login-4', methods=['GET', 'POST'])
def flashing_login():
    if request.method == 'POST':
        if request.form['password'] == 'pass':
             return redirect('success')
        else:
             flash("Naaaaaaaahhhhhhhhh")
             return render_template('login.html')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def database_register():

    try:
             
        if request.method == 'POST':
            query = "insert into users (username, password) values ('" + request.form['username'] + "'"+",'" + request.form['password'] + "')"
            cur.execute(query)
            myconn.commit()
            return redirect(url_for('database_login'))
                
        elif request.method == 'GET':
            return render_template('register.html')
    
    except:
        myconn.rollback()

    myconn.close()


@app.route("/success")
def success():
    return "logged in successfully"

if __name__ == "__main__":
    app.run(debug=True)