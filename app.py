from flask import Flask
app = Flask(__name__)

estado = 'False'

@app.route('/status')
def status_func():
    return estado

@app.route('/abrir')
def open_func():
    global estado
    estado = 'True'
    return estado

@app.route('/cerrar')
def close_func():
    global estado
    estado = 'False'
    return estado