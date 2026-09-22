from flask import Flask
app = Flask ( __name__ )

@app . route ("/")
def root ():
 return " The default, ’root ’ route"

@app . route ("/hello/")
def hello ():
    return " Hello Napier !!! :D"

@app . route ("/goodbye/")
def goodbye ():
    return " Goodbye cruel world :("