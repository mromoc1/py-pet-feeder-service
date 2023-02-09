from flask import Flask
app = Flask(__name__)

estado = 'False'

@app.route('/status')
def hello_world():
    return estado

@app.route('/abrir')
def hello_world():
    global estado
    estado = 'True'
    return estado

@app.route('/cerrar')
def hello_world():
    global estado
    estado = 'False'
    return estado