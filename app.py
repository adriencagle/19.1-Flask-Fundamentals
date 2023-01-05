# Put your app in here.
from flask import Flask, request
app = Flask(__name__)
from operations import add 
from operations import sub 
from operations import mult 
from operations import div

@app.route ('/add')
def addNum():
    aNum = int(request.args.get('a'))
    bNum = int(request.args.get('b'))
    product = add(aNum, bNum)
    return str(product)

@app.route ('/sub')
def subNum():
    aNum = int(request.args.get('a'))
    bNum = int(request.args.get('b'))
    product = sub(aNum, bNum)
    return str(product)

@app.route ('/mult')
def multNum():
    aNum = int(request.args.get('a'))
    bNum = int(request.args.get('b'))
    product = mult(aNum, bNum)
    return str(product)

@app.route ('/div')
def divNum():
    aNum = int(request.args.get('a'))
    bNum = int(request.args.get('b'))
    product = div(aNum, bNum)
    return str(product)
