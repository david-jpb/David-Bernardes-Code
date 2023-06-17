from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/person/')
def person():
    return jsonify({'name': 'Jimit', 'address': 'India'})

@app.route('/numbers/')
def print_list():
    return jsonify(list(range(5)))

@app.route('/home/')
def home():
    return "Home page"

@app.route('/contact')
def contact():
    return "Contact page"

@app.route('/teapot/')
def teapot():
    return "Would you like some tea?", 418


@app.before_request
def before():
    print("This is executed BEFORE each request.")

@app.route('/hello/')
def hello():
    return "Hello World!"

app.run()