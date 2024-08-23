from flask import Flask, request


app = Flask(__name__)


alunos = []

@app.route('/', methods=['GET'])
def joelho():

    return 'Hello World!',200

@app.route('/batata', methods=['GET'])
def batata():

    return 'DOMINAÇÃO DAS BATATAS',200

@app.route('/teste', methods=['GET'])
def teste():

    return 'Web service funcionando', 200

@app.route('/cadastro_aluno', methods=['POST'])
def cadastro():

    # entrada do usuário
    entrada_dados = request.json

    # usar caso algo não esteja funcionando
    #breakpoint()

    # adiciona o aluno na lista
    alunos.append(entrada_dados)

    #resposta para o usuário
    resp = "Aluno cadastrado com sucesso"

    return resp, 201    

@app.route('/lista_alunos', methods=['GET'])

def lista_alunos():
    resp = {
        "alunos": alunos
    }
    return resp, 200


if __name__ == '__main__':
    app.run(debug=True)