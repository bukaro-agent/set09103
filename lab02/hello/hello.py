from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def root():
    """Muestra un saludo en la página principal."""
    print ( request.method , request.path , request.form )
    return "<p>Hello Napier</p>", 200


@app.route("/account/", methods=['GET','POST'])
def account():
    """Muestra el formulario de cuenta o saluda al nombre enviado."""
    if request.method == 'POST':
        print (request.form)
        name = request.form['name']
        return "Hello %s" % name
    else:
        # En una petición GET, muestra un formulario para introducir el nombre.
        page ='''
        <html><body>
            <form action="" method="post" name="form">
                <labe for="name">Name:</label>
                <input type="text" name="name" id="name">
                <input type="submit" name="submit" id="submit"/>
            </form>
            </body><html>'''

        return page


@app.route("/hello/<name>")
def hello(name):
    """Saluda usando el nombre incluido en la URL."""
    return "Hello %s" % name

        

@app.route("/add/<int:first>/<int:second>")
def add(first, second):
    """Suma los dos números enteros incluidos en la URL."""
    return str(first+second)


@app.route("/hello2/")
def hello2():
    """Saluda con el nombre recibido como parámetro de consulta."""
    name = request.args.get('name', '')
    if name== '':
        return "no param supplied"
    else:
        return "Hello %s" % name


