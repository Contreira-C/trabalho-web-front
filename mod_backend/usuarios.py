from flask import Flask, jsonify, request
from app import *
usuarios = [
    {
        'id': 1,
        'username': 'João',
        'senha': '123456',
        'email': 'joaozinho@example.com'
    },
]
next_id = 2  # Start with the next available ID after the existing usuario

# Consultar(todos)
@app.route('/usuarios', methods=['GET'])
def obter_usuarios():
    return jsonify(usuarios)

# Consultar(id)
@app.route('/usuarios/<int:id>', methods=['GET'])
def obter_usuario_por_id(id):
    for usuario in usuarios:
        if usuario.get('id') == id:
            return jsonify(usuario)

# Editar
@app.route('/usuarios/<int:id>', methods=['PUT'])
def editar_usuario_por_id(id):
    usuario_alterado = request.get_json()
    for indice, usuario in enumerate(usuarios):
        if usuario.get('id') == id:
            usuarios[indice].update(usuario_alterado)
            return jsonify(usuarios[indice])

# Criar
@app.route('/usuarios', methods=['POST'])
def incluir_novo_usuario():
    global next_id 
    novo_usuario = request.get_json()
    novo_usuario['id'] = next_id
    next_id += 1
    usuarios.append(novo_usuario)

    return jsonify(usuarios)

# Excluir
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def excluir_usuario(id):
    for indice, usuario in enumerate(usuarios):
        if usuario.get('id') == id:
            del usuarios[indice]

    return jsonify(usuarios)