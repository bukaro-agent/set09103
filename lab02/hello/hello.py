from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def root():
    return "Hello Napier", 418

@app.route("/hello/<name>")
def hello(name):
    return "Hello %s" % name

@app.route("/account/", methods=['POST','GET'])
def account():
    if request.method == 'POST':
        print (request.form)
        name = request.form['name']
        return "Hello %s" % name
    else:
        page ='''
        <html><body>
            <form action="" method="post" name="form">
                <labe for="name">Name:</label>
                <input type="text" name="name" id="name">
                <input type="submit" name="submit" id="submit"/>
            </form>
            </body><html>'''

        return page
        

@app.route("/add/<int:first>/<int:second>")
def add(first, second):
    return str(first+second)
    
@app.route("/hello2/")
def hello2():
    name = request.args.get('name', '')
    if name== '':
        return "no param supplied"
    else:
        return "Hello %s" % name