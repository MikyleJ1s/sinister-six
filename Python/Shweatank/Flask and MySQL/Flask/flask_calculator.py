from flask import Flask, redirect, render_template, url_for, request

app = Flask(__name__)
x = 10
y = 15

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

@app.route("/user/<name>")
def greet_user(name):
    if name == "admin":
        return redirect(url_for("greet_admin"))
    else:
        return redirect(url_for("greet_guest", guest = name))

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    answer = ""
    if request.method == 'POST':
        x = float(request.form['x'])
        y = float(request.form['y']) 
        if request.form['operator'] == "+":
             return render_template('calculatorpage.html', answer=str(x+y))
        elif request.form['operator'] == "-":
             return render_template('calculatorpage.html', answer=str(x-y))
        elif request.form['operator'] == "*":
             return render_template('calculatorpage.html', answer=str(x*y))
        elif request.form['operator'] == "/" and y != 0:
             return render_template('calculatorpage.html', answer=str(x/y))
        else:
            return render_template('calculatorpage.html', answer = "Undefined")

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
