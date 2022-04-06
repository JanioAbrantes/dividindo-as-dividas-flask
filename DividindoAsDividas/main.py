from flask import Flask, render_template, request

from familia import Familia
from pessoa import Pessoa


app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/familia', methods=['GET', 'POST'])
def criar_familia():
    global familia
    if request.method == 'POST':
        familia = Familia(request.form['nome_da_familia'])
        request.method = ''
        return membros_da_familia()
    return render_template('familia.html')


@app.route('/membros', methods=['GET', 'POST'])
def membros_da_familia():
    if request.method == 'POST':
        try:
            nome_membro = request.form['nome']
            renda_membro = float(request.form['renda'])
            familia.adicionar_membros(nome_membro, renda_membro)
        except ValueError:
            return render_template('membros-da-familia.html', familia=familia.nome, membros_adicionados=familia.membros)
    print(familia.membros)
    for membros in familia.membros:
        print(membros)
    return render_template('membros-da-familia.html', familia=familia.nome, membros_adicionados=familia.membros)


@app.route('/contas')
def contas_a_pagar():
    return render_template('contas-a-pagar.html')


if __name__ == '__main__':
    app.run(debug=True)
