from flask import Flask, jsonify, request
from app import *
estoque = [
    {
        'id': 1,
        'marca': 'Nike',
        'modelo': 'Dunk',
        'cor': 'Branco',
        'tamanho': 42,
        'quantidade': 10,
        'categoria': 'Corrida'
    },
]
next_id = 2  # Start with the next available ID after the existing fornecedor

# Consultar(todos)
@app.route('/estoque', methods=['GET'])
def obter_estoque():
    return jsonify(estoque)

# Consultar(id)
@app.route('/estoque/<int:id>', methods=['GET'])
def obter_fornecedor_por_id(id):
    for fornecedor in estoque:
        if fornecedor.get('id') == id:
            return jsonify(fornecedor)

# Editar
@app.route('/estoque/<int:id>', methods=['PUT'])
def editar_fornecedor_por_id(id):
    fornecedor_alterado = request.get_json()
    for indice, fornecedor in enumerate(estoque):
        if fornecedor.get('id') == id:
            estoque[indice].update(fornecedor_alterado)
            return jsonify(estoque[indice])

# Criar
@app.route('/estoque', methods=['POST'])
def incluir_novo_fornecedor():
    global next_id 
    novo_fornecedor = request.get_json()
    novo_fornecedor['id'] = next_id
    next_id += 1
    estoque.append(novo_fornecedor)

    return jsonify(estoque)

# Excluir
@app.route('/estoque/<int:id>', methods=['DELETE'])
def excluir_fornecedor(id):
    for indice, fornecedor in enumerate(estoque):
        if fornecedor.get('id') == id:
            del estoque[indice]

    return jsonify(estoque)