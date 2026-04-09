from flask import Flask

app=Flask(__name__)

@app.route('/')
def calculator():
    return "Welcome to the Calculator App. Update the URL to perform operations."

@app.route('/add/<int:a>/<int:b>')
def add(a,b):
    return f"{a+b}"

@app.route('/subtract/<int:a>/<int:b>')
def subtract(a,b):
    return f"{a-b}"


@app.route('/multiply/<int:a>/<int:b>')
def multiply(a,b):
    return f"{a*b}"


@app.route('/divide/<int:a>/<int:b>')
def divide(a,b):
    if b==0:
        return "Error: Division by zero"
    return f"{a/b}"


if __name__=='__main__':
    app.run(debug=True)
