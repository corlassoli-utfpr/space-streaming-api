from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return 'teste'

@app.route('/videos/<string:busca>/<int:pagina>') # Busca de um vídeo por string
def buscar_videos(busca, pagina):
    return f'teste {busca} {pagina}'

@app.route('/empresas/<string:busca>/<int:pagina>') # Busca de uma empresa por string
def buscar_empresas(busca, pagina):
    return f'teste {busca} {pagina}'

@app.route('/empresas/<int:id>') # Página da empresa pelo id com seus lançamentos
def pagina_empresa(id):
    return f'teste {id}'

if __name__ == "__main__":
    app.run(port=3000, host='0.0.0.0', debug=True)
