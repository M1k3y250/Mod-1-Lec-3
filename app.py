from flask import Flask, request, jsonify

app = Flask(__name__)

# Almacenamiento en memoria
usuarios = []

# Ruta GET /info
@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        "app": "Gestor de Usuarios y Productos",
        "version": "1.0",
        "autor": "Tu Nombre",
        "descripcion": "Esta aplicacion permite gestionar usuarios y productos usando Flask."
    })

# Ruta POST /crear_usuario
@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Datos no recibidos en formato JSON"}), 400

    nombre = data.get('nombre')
    correo = data.get('correo')

    if not nombre or not correo:
        return jsonify({"error": "Faltan campos requeridos: nombre y correo"}), 400

    nuevo_usuario = {
        "id": len(usuarios) + 1,
        "nombre": nombre,
        "correo": correo
    }

    usuarios.append(nuevo_usuario)
    return jsonify({"mensaje": "Usuario creado exitosamente", "usuario": nuevo_usuario}), 201

# Ruta GET /usuarios
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify({"usuarios": usuarios})

# Manejo de error 404
@app.errorhandler(404)
def pagina_no_encontrada(e):
    return jsonify({"error": "Ruta no encontrada"}), 404

# Ejecutar el servidor
if __name__ == '__main__':
    app.run(debug=True)
