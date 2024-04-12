from flask import Flask
from urllib import request
from bs4 import BeautifulSoup

# 웹 서버 생성
app = Flask(__name__)
@app.route('/') # decorator

def hello():
    target = request.urlopen("주소")

    soup = BeautifulSoup(target, 'html.parser')