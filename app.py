from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [             # Dois Desenvolvedores Pré Cadastrados na nossa Aplicação
    {
        'id': '0',
        'Nome': 'Rafael',
        'Habilidades': ['Python', 'Flask']
     },
    {
        'id': '1',
        'Nome': 'Galleani',
        'Habilidades': ['Python', 'Django']}
]
#devolve um desenvolvedor pelo id, também altera e deleta um desenvolvedor
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])     #posso alterar, método PUT(ALTERAÇÃO); ('/dev/<int:id>/) Retornar o desenvolvedor através do ID; deixando explicito que o método é GET(RECUPERANDO)...só aceita o GET
def desenvolvedor(id):
    #para diferenciar o get do put....
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]   #ID é a posição no dicionário
        except IndexError:
           mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
           response = {'Status': 'Erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'Status': 'Erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)       #json.loads -> transformando a requisição em json; dados recebe um JSON dentro do body no POSTMAN
        desenvolvedores[id] = dados
        return jsonify(dados)   #retornando o que foi alterado
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'Status': 'Sucesso', 'Mensagem': 'Registro Excluído'})


#Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':     #fazendo a inserção
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)

#PUT -> é usado para enviar e armazenar uma informação!
#POST -> pressupõe que as informações são apenas parte do processo, não o todo!
#GET -> faz um pedido de pesquisa
#PUT -> faz a inserção de novos elementos