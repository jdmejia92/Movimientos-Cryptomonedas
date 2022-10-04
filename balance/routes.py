from balance import app
from flask import render_template


ruta_db = app.config['RUTA_BBDD']

@app.route("/")
def start():
    return render_template("index.html")