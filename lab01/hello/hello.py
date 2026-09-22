from flask import Flask
app = Flask ( __name__ )

@app . route ("/")
def hello ():
    return """
    <p> Hello , World ! </p>
    <script>
        const name = 'Jaime A.';
        const surename = 'Garcia';
        document.write(`My full name is ${name} ${surename}`);
    </script>
    """



if __name__ == "__main__":
    app.run(debug=True)