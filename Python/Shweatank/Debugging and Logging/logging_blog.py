from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(filename="record.log", level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route('/add')
def func(x):
    return x +2

@app.route('/blog')

def blog():
    app.logger.info("Info Log")
    app.logger.warning("Warning Log")
    return f"Welcome to the blog"

def test_answer():
    assert blog() == "Welcome to the blog"
    
if __name__ == '__main__':
    app.run()