from flask import Flask

app = Flask(__name__)
@app.route('/welcome')
def welcomePage():
    html = "<html><body><h1>welcome</h1></body></html>"
    return html

@app.route('/welcome/home')
def welcomeHome():
    html = "<html><body><h1>welcome home</h1></body></html>"
    return html

@app.route('/welcome/back')
def welcomeBack():
    html = "<html><body><h1>welcome back</h1></body></html>"
    return html