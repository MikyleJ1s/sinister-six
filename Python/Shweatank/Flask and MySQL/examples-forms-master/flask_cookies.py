from flask import *
app = Flask(__name__)

@app.route('/error')
def error():
    return "<p><strong>Enter the correct password</strong></p>"

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/success', methods = ['GET', 'POST'])
def success():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
    
    if password == 'pass':
        resp = make_response(render_template('success.html'))
        resp.set_cookie('email', email)
        
        return resp
    else:
        return redirect(url_for('error'))
    
@app.route('/viewprofile')
def profile():
    email = request.cookies.get('email')
    resp = make_response(render_template('profile.html', name = email))
    return resp

if __name__ == '__main__':
    app.run(debug=True)
    
'''
from flask import Flask 
from flask import make_response 
app = Flask(__name__) 
app.make_response("Hello World")
    '''