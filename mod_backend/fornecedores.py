from flask import Flask, jsonify, request
from app import *
fornecedores = [
    {
        'id': 1,
        'nome': 'Nike',
        'email': 'teste@example.com',
        'cnpj': '00.000.000/0001-00',
        'telefone': '(00)00000-0000',
        'categoria': 'Fabricante',
    },
]
next_id = 2  # Start with the next available ID after the existing item

# Consultar(todos)
@app.route('/fornecedores', methods=['GET'])
def obter_fornecedores():
    return jsonify(fornecedores)

# Consultar(id)
@app.route('/fornecedores/<int:id>', methods=['GET'])
def obter_item_por_id(id):
    for item in fornecedores:
        if item.get('id') == id:
            return jsonify(item)

# Editar
@app.route('/fornecedores/<int:id>', methods=['PUT'])
def editar_item_por_id(id):
    item_alterado = request.get_json()
    for indice, item in enumerate(fornecedores):
        if item.get('id') == id:
            fornecedores[indice].update(item_alterado)
            return jsonify(fornecedores[indice])

# Criar
@app.route('/fornecedores', methods=['POST'])
def incluir_novo_item():
    global next_id 
    novo_item = request.get_json()
    novo_item['id'] = next_id
    next_id += 1
    fornecedores.append(novo_item)

    return jsonify(fornecedores)

# Excluir
@app.route('/fornecedores/<int:id>', methods=['DELETE'])
def excluir_item(id):
    for indice, item in enumerate(fornecedores):
        if item.get('id') == id:
            del fornecedores[indice]

    return jsonify(fornecedores)