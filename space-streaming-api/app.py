from flask import Flask
from controllers import empresasCtrl
from controllers import videosCtrl

app = Flask(__name__)

@app.route('/')
def root():
    return 'teste'

@app.route('/videos/<string:busca>/<int:pagina>')
def buscar_videos(busca, pagina):
    return videosCtrl.buscar(busca, pagina)

@app.route('/empresas/<string:busca>/<int:pagina>')
def buscar_empresas(busca, pagina):
    return empresasCtrl.buscar(busca, pagina)

@app.route('/empresas/<int:id>')
def pagina_empresa(id):
    return empresasCtrl.pagina(id)

if __name__ == "__main__":
    app.run(port=3000, host='0.0.0.0', debug=True, use_reloader=False)