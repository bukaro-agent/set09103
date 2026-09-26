from flask import Flask, request
import random
app = Flask(__name__)

# La ruta principal muestra el formulario y procesa las tiradas.
@app.route("/", methods=["GET", "POST"])
def dice():
    # POST se ejecuta cuando se envía el formulario.
    if request.method == "POST":
        try:
            # Lee del formulario la cantidad de dados y la convierte a entero.
            number_of_dice = int(request.form["number_of_dice"])
        except (KeyError, ValueError):
            # Devuelve un error si falta el dato o no es un número válido.
            return "Not valid value", 400

        if number_of_dice < 1:
            return "At least one dice to roll" , 400

        # Genera un resultado aleatorio del 1 al 6 por cada dado.
        rolls = [random.randint(1,6) for _ in range (number_of_dice)]
        results = ", ".join(str(roll) for roll in rolls)

        # Devuelve la página con los resultados y un enlace para volver.
        return f'''
            <h1>Results</h1>
            <p>{results}</p>
            <a href="/">Try again</a>'''
    
    # GET muestra el formulario para indicar cuántos dados tirar
    return '''
        <html><body>
            <h1>DICE WEB APP</h1>
            <form action="/" method="post" name="form">
                <label for="number_of_dice">Number of dice:</label>
                <input type="number" name="number_of_dice" id="number_of_dice">
                <input type="submit" name="submit" id="submit"/>
            </form>
            </body><html>'''