from flask import Flask

app = Flask(__name__)

@app.route('/<int:number>/')
def incrementer(number):
    return "Incremented number is" + str(number+1)

@app.route('/<string:name>/')
def hello(name):
    return "hello " + name


app.run()

# http://localhost:5000/Mike/