from flask import Flask, render_template
from controllers import empresasCtrl
from controllers import videosCtrl

app = Flask(__name__)

@app.route('/') # Rota com a página princial do front que consome os dados
def root():
    return render_template('index.html')

@app.route('/videos/<string:busca>/<int:pagina>') # Rota de busca por string, com paginação em até 5 vídeos por página
def buscar_videos(busca, pagina):
    return videosCtrl.buscar(busca, pagina)

@app.route('/empresas/<string:busca>') # Rota de busca por string das empresas, sem paginação
def buscar_empresas(busca):
    return empresasCtrl.buscar(busca)

@app.route('/empresas/<int:id>') # Rota de uma empresa específica encontrada pelo seu id
def pagina_empresa(id):
    return empresasCtrl.pagina(id)

if __name__ == "__main__":
    app.run(port=3000, host='0.0.0.0', debug=True, use_reloader=False) 
    # Removemos o reloader pois ao recarregar o código solicitava a senha do banco múltiplas vezes no desenvolvimento