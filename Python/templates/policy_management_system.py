import mysql.connector
from Logic import DatabaseUser
from flask import Flask, redirect, render_template, url_for, request
obj = DatabaseUser("localhost","root","Neville123","test_schema")

app = Flask(__name__)
user_id = ''
@app.route("/")
def form():
    return render_template("login_page.html")
@app.route('/data/', methods=['GET', 'POST'])
def user_login():
    if request.method == "POST":
        form_data = request.form
        password = form_data.get("Password")
        username = form_data.get("Username")
        if obj.isValidUser(username, password):
            return render_template('policies_page.html',form_data = form_data)
        else:
            return render_template('val.html', form_data = form_data)   

if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=80)
    app.run(debug=True)