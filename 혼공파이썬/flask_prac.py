from flask import Flask

app = Flask(__name__)


@app.route('/') # decorator
def hello():
    return "<h1>hello world!</h1>"