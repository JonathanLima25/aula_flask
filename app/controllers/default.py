from app import app


@app.route('/index')
@app.route('/')
def index():
    return 'Hello world'

@app.route('/test')
@app.route('/test/<name>')
def teste(name=None):
    if name:
        return '<h1>Olá, %s!</h1>' %name
    else:
        return '<h1>Olá!</h1>'