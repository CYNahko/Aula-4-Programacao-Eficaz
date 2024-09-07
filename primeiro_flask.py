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

    # verifica se as chaves foram digitadas corretamente
    chaves = ['nome', 'idade', 'cpf']
    for chave in chaves:
        if chave not in entrada_dados.keys():
            resp = 'Chave incorreta, o correto é:',{chave}
            return resp,400
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
            return aluno,200
    return 'Aluno não encontrado',400
        
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
    chaves = ['nome', 'quantidade de aulas por semana', 'curso']
    for chave in chaves:
        if chave not in entrada_dados.keys():
            resp = 'Chave incorreta, o correto é:',{chave}
            return resp,400
    disciplina_id = len(disciplinas) + 1
    entrada_dados['id'] = disciplina_id
    disciplinas.append(entrada_dados)
    return "Disciplina cadastrada com sucesso!", 200

@app.route('/disciplina/<int:id>',methods=['DELETE'])
def deletar_disciplina(id):
    for disciplina in disciplinas:
        if disciplina['id'] == id:
            disciplinas.remove(disciplina)
            return 'Disciplina deletada com sucesso.', 200
        
@app.route('/disciplina/<int:id>',methods=['GET'])
def busca_disciplina(id):
    for disciplina in disciplinas:
        if disciplina['id'] == id:
            return disciplina,200
    return 'Disciplina não encontrada.', 400

@app.route('/disciplina/<int:id>',methods=['PUT'])
def atualiza_disciplina(id):
    atualiza_dados = request.json
    for disciplina in disciplinas:
        if disciplina['id'] == id:
            disciplina['nome'] = atualiza_dados['nome']
            disciplina['quantidade de aulas por semana'] = atualiza_dados['quantidade de aulas por semana']
            disciplina['curso'] = atualiza_dados['curso']
            return 'Dados atualizados com sucesso.', 200

@app.route('/matricula',methods=['GET'])
def lista_matriculas():
    resp = {
        'matriculas': matriculas
    }
    return resp, 200

@app.route('/matricula', methods=['POST'])
def criar_matricula():
    entrada_dados = request.json
    chaves = ['id_aluno', 'id_disciplina']
    # verifica se as chaves existem
    for chave in chaves:
        if chave not in entrada_dados.keys():
            resp = 'Chave incorreta, o correto é:',{chave}
            return resp,400
    # após confirmar que existem, verificam por id_aluno
    for aluno in alunos:
        if entrada_dados['id_aluno'] == aluno['id']:
            if chaves[1] in entrada_dados.keys():
                for disciplina in disciplinas:
                    if entrada_dados['id_disciplina'] == disciplina['id']:
                        id_matricula = len(matriculas) + 1
                        entrada_dados['id'] = id_matricula
                        matriculas.append(entrada_dados)
                        resp = 'Matricula cadastrada com sucesso.'
                        return resp, 201
                return 'ID de disciplina inexistente.',400
                    
@app.route('/matricula/<int:id_aluno>',methods=['GET'])
def buscar_matricula(id_aluno):
    aluno_matriculado = []
    for matricula in matriculas:
        if matricula['id_aluno'] == id_aluno:
            aluno_matriculado.append(matricula)
    return aluno_matriculado, 200

@app.route('/matricula/<int:id>',methods=['DELETE'])
def deletar_matricula(id):
    for matricula in matriculas:
        if matricula['id'] == id:
            matriculas.remove(matricula)
            return 'Matricula deletada com sucesso.',200

if __name__ == '__main__':
    app.run(debug=True)