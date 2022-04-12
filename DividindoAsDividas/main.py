from flask import Flask, redirect, render_template, request, url_for

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
            return render_template('membros-da-familia.html', nome_familia=familia.nome, membros_adicionados=familia.membros,
                                   renda_total=familia.renda_total)
        except NameError:
            return render_template('index.html')
    try:
        return render_template('membros-da-familia.html', nome_familia=familia.nome, membros_adicionados=familia.membros,
                               renda_total=familia.renda_total)
    except NameError:
        return redirect(url_for('homepage'))


@app.route('/contas', methods=['GET', 'POST'])
def contas_a_pagar():
    if request.method == 'POST':
        try:
            nome_conta = request.form['conta']
            valor_conta = float(request.form['valor'])
            familia.calcular_pagamentos_mensais(nome_conta, valor_conta)
        except ValueError:
            return render_template('contas-a-pagar.html', nome_familia=familia.nome,
                                   contas_adicionadas=familia.contas_a_pagar, total_a_pagar=familia.pagamentos_mensais,
                                   membros_adicionados=familia.membros, renda_total=familia.renda_total)
        except NameError:
            return redirect(url_for('homepage'))
    try:
        return render_template('contas-a-pagar.html', nome_familia=familia.nome, contas_adicionadas=familia.contas_a_pagar,
                               total_a_pagar=familia.pagamentos_mensais, membros_adicionados=familia.membros,
                               renda_total=familia.renda_total)
    except NameError:
        return redirect(url_for('homepage'))


@app.route('/dividas-divididas')
def dividir_dividas():
    try:
        global familia
        return render_template('dividas-divididas.html', familia=familia, contas_adicionadas=familia.contas_a_pagar,
                               total_a_pagar=familia.pagamentos_mensais, membros_adicionados=familia.membros,
                               renda_total=familia.renda_total, nome_familia=familia.nome)
    except NameError:
        return redirect(url_for('homepage'))


if __name__ == '__main__':
    app.run()
