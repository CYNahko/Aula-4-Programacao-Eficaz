from flask import Flask, request


app = Flask(__name__)


alunos = []
disciplinas = []
matriculas = []

@app.route('/', methods=['GET'])
def joelho():

    return 'Hello World!',200

@app.route('/batata', methods=['GET'])
def batata():

    return 'DOMINAÇÃO DAS BATATAS',200

@app.route('/teste', methods=['GET'])
def teste():

    return 'Web service funcionando', 200

@app.route('/aluno', methods=['POST'])
def cadastro():

    # entrada do usuário
    entrada_dados = request.json
    entrada_dados_dict = dict(entrada_dados)

    # verifica se as chaves foram digitadas corretamente
    if entrada_dados_dict["nome"] not in entrada_dados:
        return "Chave inválida. O correto é 'nome'",400
    elif entrada_dados_dict["idade"] not in entrada_dados:
        return "Chave inválida. O correto é 'idade'",400
    elif entrada_dados_dict["cpf"] not in entrada_dados:
        return "Chave inválida. O correto é 'cpf'"
    else:
        entrada_dados['id'] = len(alunos)+1
        # adiciona o aluno na lista
        alunos.append(entrada_dados)

    #resposta para o usuário
    resp = "Aluno cadastrado com sucesso"

    return resp, 201    

@app.route('/aluno', methods=['GET'])

def lista_alunos():
    resp = {
        "alunos": alunos
    }
    return resp, 200


@app.route('/aluno/<int:id>', methods=['DELETE'])
def deletar_aluno(id):
    id_aluno = id
    for aluno in alunos:
        if aluno['id'] == id_aluno:
            alunos.remove(aluno)
            return "Aluno deletado com sucesso.",200

@app.route('/aluno/<int:id>', methods=['GET'])
def buscar_aluno(id):
    for aluno in alunos:
        if aluno['id'] == id:
            return aluno
        
@app.route('/aluno/<int:id>', methods=['PUT'])
def atualizar_aluno(id):
    atualizado = request.json
    if alunos == []:
        return "ID inexistente", 400
    else:
        for aluno in alunos:
            if id == aluno["id"]:
                aluno["nome"] = atualizado["nome"]
                aluno["idade"]  = atualizado["idade"]
                aluno["cpf"] = atualizado["cpf"]
                return "Dados atualizados com sucesso.",200

@app.route('/disciplina', methods=['GET'])
def lista_disciplinas():
    resp = {
        "disciplinas": disciplinas
    }
    return resp, 200

@app.route('/disciplina',methods=['POST'])
def cadastro_disciplina():
    entrada_dados = request.json
    disciplina_id = len(disciplinas) + 1

    



if __name__ == '__main__':
    app.run(debug=True)