from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return 'teste'

@app.route('/videos/<string:busca>/<int:pagina>')
def f1(busca, pagina):
    return f'teste {busca} {pagina}'

@app.route('/videos/<int:id>')
def f2(id):
    return f'teste {id}'

@app.route('/lancamentos/<string:busca>/<int:pagina>')
def f3(busca, pagina):
    return f'teste {busca} {pagina}'

@app.route('/lancamentos/<int:id>')
def f4(id):
    return f'teste {id}'

@app.route('/lancamentos/<int:id>/videos')
def f5(id):
    return f'teste {id}'

@app.route('/empresas/<string:busca>/<int:pagina>')
def f6(busca, pagina):
    return f'teste {busca} {pagina}'

@app.route('/empresas/<int:id>')
def f7(id):
    return f'teste {id}'

if __name__ == "__main__":
    app.run(port=3000, host='0.0.0.0', debug=True)