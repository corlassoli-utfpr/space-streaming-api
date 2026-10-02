from flask import Flask
from controllers import empresasCtrl
from controllers import videosCtrl

app = Flask(__name__)

@app.route('/')
def root():
    return 'teste'

@app.route('/videos/<string:busca>/<int:pagina>') # Como temos 10 vídeos, a paginação divide em no máximo 5 por página
def buscar_videos(busca, pagina):
    return videosCtrl.buscar(busca, pagina)

@app.route('/empresas/<string:busca>') # Sem paginação pois temos apenas 5 empresas, logo não temos conteúdo suficiente para completar uma segunda página
def buscar_empresas(busca):
    return empresasCtrl.buscar(busca)

@app.route('/empresas/<int:id>')
def pagina_empresa(id):
    return empresasCtrl.pagina(id)

if __name__ == "__main__":
    app.run(port=3000, host='0.0.0.0', debug=True, use_reloader=False)