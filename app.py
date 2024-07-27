from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def acerca():
    return render_template('acerca.html')

@app.route('/boyaca')
def Boyaca():
    return render_template('boyaca.html')

@app.route('/cundinamarca')
def cundinamarca():
    return render_template('cundinamarca.html')

@app.route('/flora')
def flora():
    return render_template('flora.html')

@app.route('/fauna')
def fauna():
    return render_template('fauna.html')

@app.route('/Geolocalizacion')
def Geolocalizacion():
    return render_template('Geolocalizacion.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/biodiversidad')
def biodiversidad():
    return render_template('biodiversidad.html')

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/municipios')
def municipios():
    return render_template('municipios.html')

if __name__ == '__main__':
    app.run(debug=True)