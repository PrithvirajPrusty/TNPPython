from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    num1 = request.args.get('num1', type=str)
    num2 = request.args.get('num2', type=str)
    return f"Addition of 2 numbers {num1} + {num2}"

@app.route("/sub")
def sub():
    num1 = request.args.get('num1', type=str)
    num2 = request.args.get('num2', type=str)
    return f"Subtraction of 2 numbers {num1} + {num2}"

@app.route("/mul")
def mul():
    num1 = request.args.get('num1', type=str)
    num2 = request.args.get('num2', type=str)
    return f"Multiplication of 2 numbers {num1} + {num2}"

@app.route("/home")
def home():
    return "<h1>Hello</h1>"

if __name__ == '__main__':
    app.run(debug=True)