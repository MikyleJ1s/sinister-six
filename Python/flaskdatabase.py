import mysql.connector
from flask import Flask, redirect, render_template, url_for, request

app = Flask(__name__)
myconn = mysql.connector.connect(host="localhost", user="root", passwd="Mikyle123", database="policy_management_system")
cur = myconn.cursor()
    
@app.route('/login', methods=['GET', 'POST'])
def user_login():


    try:
        #dbs = cur.execute("create table users(username varchar(20) not null, id int not null primary key, password varchar(50) not null)")
        #cur.execute("insert into users values ('Bob', 1, 'bobby'), ('Tom', 2, '123'),('Meg', 3, 'passwrd')")
        
        error = "" 
             
        if request.method == 'POST':

            query = "select * from users where username = '" + request.form['username'] + "' and password = '" + request.form['password'] + "'"
            
            cur.execute(query)
            useraccount = cur.fetchone()
            
            if useraccount:
                return redirect(url_for('user_home'))
            else: 
                return render_template('login_page.html', error='Invalid Credentials.')
                
            
        elif request.method == 'GET':
            return render_template('login_page.html', error='')
        return render_template('login_page.html', error='')
    
    except:
        myconn.rollback()
    myconn.close()

@app.route("/home")
def user_home():
    return render_template('home_page.html')

@app.route("/uploaded", methods = ['POST'])
def uploaded():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return render_template('confirmupload.html', confirm="uploaded successfully")

if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=80)
    app.run(debug=True)