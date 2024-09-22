from flask import Flask, url_for
import random
import os
app = Flask(__name__)

@app.route("/")
def hello_world():
    return """<h1>Hello, World!</h1>
    <ul>
    <li><a href="/numero">¡Ver un número aleatorio!</a></li>
    <li><a href="/letra">¡Ver una letra aleatoria!</a></li>
    <li><a href="/dato">¡Ver un dato aleatorio!</a></li>
    <li><a href="/moneda">¡Moneda al azar - Cara o sello!</a></li>
    <li><a href="/contraseña">¡Contraseña al azar!</a></li>
    <li><a href="/imagen">¡Imagen generada al azar!</a></li>
    </ul>
    """
@app.route("/numero")
def numero():
    num = random.randint(1,100)
    return f"El numero es {num}"

@app.route("/letra")
def abc():
    lista = ("abcdefghijklmnñopqrstuvwxyz")
    letras = random.choice(lista)
    return f"La letra es {letras}"

@app.route("/dato")
def datos():
    lista_datos = [""
    "El español es el segundo idioma más hablado del mundo. Por detrás del chino.",
    "Si el cerebro humano fuera un ordenador, podría realizar 38.000 billones de operaciones por segundo.",
    "El ADN humano es idéntico al ADN de un plátano en un 50%.",
    "Los dientes humanos son casi tan duros como las piedras.",
    "Uno puede morirse de risa. Puede provocar un infarto...",
    "Nuestro aroma es tan único como nuestras huellas. No hay dos iguales."
                    ""]
    return f'<p>{random.choice(lista_datos)}</p>'

@app.route("/moneda")
def moneda():
    eleccion = ("Cara", "Sello")
    resultado = random.choice(eleccion)
    return f"El lado de la moneda es: {resultado}"

@app.route("/contraseña")
def contra():
    contraseña = ("")
    caracteres = ("abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
    longitud = (12)
    for i in range(longitud):
        contraseña += random.choice(caracteres)
    return f"La contraseña generada es: {contraseña}"

@app.route("/imagen")
def imagen():
    # Asegúrate de que las imágenes estén en la carpeta static/images
    image_folder = os.path.join(app.static_folder, 'images')
    imagenes = os.listdir(image_folder)  # Cargamos las imágenes de la carpeta static/images
    imagen_aleatoria = random.choice(imagenes)
    return f'<img src="{url_for("static", filename=f"images/{imagen_aleatoria}")}" alt="Imagen aleatoria">'

app.run(debug=True)
