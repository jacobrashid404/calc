from operations import add, sub, mult, div
from flask import Flask, request
app = Flask(__name__)


@app.get('/add')
def add_numbers():
    """takes in 2 numbers and return their sum"""

    a = int(request.args["a"])
    b = int(request.args["b"])

    sum = str(add(a, b))

    return sum


@app.get('/sub')
def subtract_numbers():
    """takes in 2 numbers and return their difference"""

    a = int(request.args["a"])
    b = int(request.args["b"])

    difference = str(sub(a, b))

    return difference


@app.get('/mult')
def multiply_numbers():
    """takes in 2 numbers and return their difference"""

    a = int(request.args["a"])
    b = int(request.args["b"])

    product = str(mult(a, b))

    return product


@app.get('/div')
def divide_numbers():
    """takes in 2 numbers and return their difference"""

    a = int(request.args["a"])
    b = int(request.args["b"])

    quotient = str(div(a, b))

    return quotient
