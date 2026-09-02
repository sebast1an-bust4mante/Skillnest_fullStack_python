import random
from flask import Flask, redirect, render_template, request, session, url_for
from datetime import date

app = Flask(__name__)
app.secret_key = "clave_secreta"

# Mensajes de predicción principal
PREDICCIONES = [
    "Encontrarás el verdadero amor en los próximos meses. Tu corazón se llenará de alegría.",
    "Un cambio significativo en tu carrera te traerá prosperidad y reconocimiento.",
    "Un viaje inesperado te abrirá nuevas puertas y perspectivas de vida.",
    "Tu creatividad florecerá, permitiéndote resolver un problema que te ha preocupado.",
    "Nuevas amistades sinceras y duraderas están por llegar a tu vida."
]

# Definiciones para colores y animales (para el texto personalizado)
INFO_COLORES = {
    'rojo': 'pasión y energía',
    'azul': 'calma y sabiduría',
    'verde': 'misterio y descubrimiento',
    'morado': 'espiritualidad y ambición',
    'amarillo': 'alegría e intelecto',
    'negro': 'poder y elegancia',
    'blanco': 'pureza y nuevos comienzos'
}

INFO_ANIMALES = {
    'perro': 'lealtad y protección',
    'gato': 'independencia y misterio',
    'águila': 'visión y libertad',
    'león': 'fuerza y coraje',
    'delfín': 'inteligencia y armonía',
    'búho': 'sabiduría e intuición',
    'lobo': 'instinto y comunidad'
}

@app.route("/")
def index():
    # Limpiar sesión si vuelven al inicio
    session.clear()
    return render_template("index.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    session["nombre"] = request.form.get("nombre")
    session["edad"] = request.form.get("edad")
    session["color"] = request.form.get("color").lower() # Guardar en minúsculas
    session["animal"] = request.form.get("animal").lower() # Guardar en minúsculas
    return redirect(url_for("futuro"))

@app.route("/futuro")
def futuro():
    if "nombre" not in session:
        return redirect(url_for("index"))

    # Lógica de la predicción
    prediccion_principal = random.choice(PREDICCIONES)
    
    # Datos personalizados
    color_usuario = session.get("color")
    animal_usuario = session.get("animal")
    
    # Buscar significados (con fallback si no está en la lista)
    significado_color = INFO_COLORES.get(color_usuario, 'un camino único por descubrir')
    significado_animal = INFO_ANIMALES.get(animal_usuario, 'una guía especial y personal')
    
    # Número de la suerte
    numero_suerte = random.randint(1, 100)
    
    # Fecha de hoy
    hoy = date.today().strftime("%B %d, %Y")

    return render_template(
        "futuro.html",
        nombre=session.get("nombre"),
        edad=session.get("edad"),
        color=color_usuario,
        significado_color=significado_color,
        animal=animal_usuario,
        significado_animal=significado_animal,
        prediccion_principal=prediccion_principal,
        numero_suerte=numero_suerte,
        fecha_hoy=hoy
    )

if __name__ == "__main__":
    app.run(debug=True)