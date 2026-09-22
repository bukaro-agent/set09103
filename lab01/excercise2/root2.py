from flask import Flask, redirect, url_for
import random
app = Flask(__name__)

@app.route ("/")
def root ():
    if random.randint(1, 100) <= 10:
        return redirect(url_for("ten"))
    return redirect(url_for("ninety"))

@app.route ("/ten")
def ten ():
    return " Hello Napier !!! :D"

@app.route ("/ninety")
def ninety ():
    return " Goodbye cruel world :("