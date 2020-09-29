from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades
import json

app = Flask(__name__)
api = Api(app)

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

#em vez da rota e o nome da função, agora temos uma classe
#devolve um desenvolvedor pelo id, também altera e deleta um desenvolvedor
class Desenvolvedor(Resource):      #função resource como parâmetro
    def get(self, id):                  #dentro das classes temos os métodos
        if request.method == 'GET':
            try:
                response = desenvolvedores[id]
            except IndexError:
                mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
                response = {'Status': 'Erro', 'mensagem': mensagem}
            except Exception:
                mensagem = 'Erro desconhecido. Procure o administrador da API'
                response = {'Status': 'Erro', 'mensagem': mensagem}
            return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluido'}

#Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def get (self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores

#na parte da rota:
api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)

