from flask import Flask, render_template

from . import prime
from . import random_name as rn

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/json/')
def json():
    return {"hello": "world"}


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    if name is None:
        name = "Anonymous"
    return render_template("hello.html", name=name)


@app.route('/hello/random')
def hello_random():
    return render_template("hello.html", name=rn.random_name())


@app.route('/isPrime/')
@app.route('/isPrime/<int:n>')
def primes(n=None):
    if n is None or n == 0:
        return render_template("is-prime.html")
    if n > 1000:
        return "Please select a natural number lower or equal to 1000."
    # Return prime.html with list of prime numbers
    return render_template("is-prime.html", n=str(n),
                           isPrime=bool(prime.is_prime(n)))


@app.route('/getPrime/')
@app.route('/getPrime/<int:n>')
def nth_prime(n=None):
    # return n-th prime number
    if n is None or n == 0:
        return render_template("nth-prime.html")
    if n > 1000:
        return "Please select a natural number lower or equal to 1000."
    # Return prime.html with list of prime numbers
    return render_template("nth-prime.html", n=str(n),
                           prime=str(prime.get_nth_prime(n)))
