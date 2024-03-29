from flask import Flask, render_template, request, flash
from flask_wtf import form
from form import ContactForm

app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash("ALL FIELDS ARE REQUIRED!")
            return render_template('contact.html', form = form)
        else:
            return render_template('success.html')
    elif request.method == 'GET':
        return render_template('contact.html', form=form)
    
@app.route('/success', methods = ['GET', 'POST'])
def success():
    return render_template('success.html')
    
if __name__ == '__main__':
    app.run(debug = True)