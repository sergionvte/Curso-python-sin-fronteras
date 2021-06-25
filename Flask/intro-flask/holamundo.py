from flask import Flask, request, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return 'hola mundo'

# GET, POST, PUT, PATCH, DELETE
@app.route('/post/<post_id>', methods=['GET', 'POST'])
def lala(post_id):
    if request.method == 'GET':
        return 'El id del post es: ' + post_id
    else:
        return 'Este es otro método y no GET'

@app.route('/lele', methods=['POST'])
def lele():
    print(url_for('lala', post_id=2))
    print(request.form)
    print(request.form['llave1'])
    print(request.form['llave2'])
    return 'lele'
