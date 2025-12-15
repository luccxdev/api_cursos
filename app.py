from flask import Flask, jsonify, request

app = Flask(__name__)
cursos = []

@app.route('/cursos', methods=['GET'])
def listar_cursos():
    return jsonify(cursos), 200

@app.route('/cursos', methods=['POST'])
def criar_curso():
    dados = request.get_json()
    if not dados or not isinstance(dados, dict):
        return jsonify({"erro": "JSON inválido"}), 400
    campos_obrigatorios = ["nome", "professor"]
    for campo in campos_obrigatorios:
        if campo not in dados:
            return jsonify({"erro": f"Campo '{campo}' é obrigatório"}), 400
    novo_curso = {"id": len(cursos) + 1, "nome": dados["nome"], "professor": dados["professor"]}
    cursos.append(novo_curso)
    return jsonify(novo_curso), 201
@app.route('/cursos/<int:id>', methods=['PUT'])
def atualizar_curso(id):
    for curso in cursos:
        if curso['id'] == id:
            curso.update(request.get_json())
            return jsonify(curso), 200
    return jsonify({'erro': 'Curso não encontrado'}), 404

@app.route('/cursos/<int:id>', methods=['DELETE'])
def deletar_curso(id):
    for i, curso in enumerate(cursos):
        if curso['id'] == id:
            cursos.pop(i)
            return jsonify({'mensagem': 'Curso deletado'}), 200
    return jsonify({'erro': 'Curso não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
