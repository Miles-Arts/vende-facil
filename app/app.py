# Importar las bibliotecas necesarias de Flask
# Flask: Framework principal
# render_template: Para renderizar plantillas HTML
# request: Para manejar solicitudes HTTP
# url_for, redirect: Para redirecciones y generación de URLs dinámicas
from flask import Flask 
from flask import render_template
from flask import request
from flask import url_for, redirect
from flask import jsonify
#from src.conexion_postgresql import obtener_conexion
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.conexion_postgresql import obtener_conexion

app=Flask(__name__)


# Middleware que se ejecuta antes de cada solicitud
@app.before_request
def before_request():
    # Imprime un mensaje antes de procesar la solicitud
    print("Antes de la petición...")

# Middleware que se ejecuta después de cada solicitud
@app.after_request
def after_request(response):
    # Imprime un mensaje después de procesar la solicitud
    print("Despues de la petición...")
    # Devuelve la respuesta al cliente
    return response

# Ruta principal de la aplicación
@app.route('/')
def index():
    # Lista de cursos disponibles
    cursos=["PHP", "Python", "Java", "Go", "Cobol", "C++"]
    # Diccionario con datos para pasar a la plantilla HTML
    data={
        'titulo': 'Inicio',
        'bienvenida': 'Holaaa',
        "cursos": cursos,
        "numero_cursos": len(cursos)
    }
    # Renderiza la plantilla 'index.html' con los datos proporcionados
    return render_template('index.html', data=data)

# Ruta para la página de contacto con parámetros dinámicos
@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre, edad):
    # Diccionario con datos para pasar a la plantilla HTML
    data={
        'titulo': 'Contacto',
        'nombre': nombre,
        'edad': edad
    }
    # Renderiza la plantilla 'contacto.html' con los datos proporcionados
    return render_template('contacto.html', data=data)

# Ruta para manejar parámetros de consulta (query string)
def query_string():
    # Imprime la solicitud completa
    print(request)
    # Imprime los parámetros de consulta
    print(request.args)
    # Obtiene y muestra el valor del parámetro 'param1'
    print(request.args.get('param1'))
    # Obtiene y muestra el valor del parámetro 'param2'
    print(request.args.get('param2'))
    # Devuelve una respuesta simple
    return 'ok'



@app.route('/asignaturas')
def asignaturas():
    data = []
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT codigo, nombre, creditos FROM asignaturas ORDER BY nombre ASC")
        rows = cursor.fetchall()
        # Convertir los resultados a una lista de diccionarios
        data = [
            {"codigo": row[0], "nombre": row[1], "creditos": row[2]}
            for row in rows
        ]
        cursor.close()
        conn.close()
    except Exception as ex:
        return jsonify({"error": str(ex)})
    return jsonify(data)

# Manejo de errores 404 (página no encontrada)
def pagina_no_encontrada(error):
    # Redirige al índice en caso de error 404
    return redirect(url_for('index'))

# Punto de entrada principal de la aplicación
if __name__=="__main__":
    # Agrega la ruta para manejar parámetros de consulta
    app.add_url_rule('/query_string', view_func=query_string)
    # Registra el manejador de errores 404
    app.register_error_handler(404,pagina_no_encontrada)
    # Ejecuta la aplicación Flask en modo de depuración y en el puerto 5000
    app.run(debug=True, port=5000)
