from flask import Flask, redirect, render_template, request, url_for

from familia import Familia
from pessoa import Pessoas
from conta import Contas

app = Flask(__name__)

familia = Familia('')
pessoa = Pessoas()
conta = Contas()
calculo_individual = False


@app.route('/')
def homepage():
    return render_template(
        'index.html',
        nome_familia=familia.nome,
        membros_adicionados=pessoa.nomes,
        rendas_adicionadas=pessoa.rendas,
        contas_adicionadas=conta.nomes,
        valores_adicionados=conta.valores,
        monetizar=monetizar,
        renda_total=sum(pessoa.rendas),
        total_contas=sum(conta.valores),
        calculo_individual=calculo_individual,
        dividas_divididas=familia.calcular_pagamento_individual
    )


@app.route('/', methods=['POST'])
def criar_familia():
    global familia
    if request.method == 'POST' and familia.nome == '' and request.form['nome_da_familia'].strip() != '':
        familia = Familia(request.form['nome_da_familia'])
    return homepage()


@app.route('/nome-membros', methods=['GET', 'POST'])
def membros_nome():
    if request.method == 'POST':
        try:
            nome_membro = request.form['nome_do_membro'].strip().capitalize()
            if nome_membro not in pessoa.nomes and nome_membro != '':
                pessoa.adicionar_nome(nome_membro)
        except NameError:
            pass
    return homepage()


@app.route('/renda-membros', methods=['GET', 'POST'])
def membros_renda():
    if request.method == 'POST':
        try:
            renda_membro = float(request.form['renda_mensal'])
            if renda_membro >= 0:
                pessoa.adicionar_renda(renda_membro)
        except ValueError:
            pass
    return homepage()


@app.route('/contas', methods=['GET', 'POST'])
def contas_a_pagar():
    if request.method == 'POST':
        try:
            nova_conta = request.form['nome_conta'].strip().capitalize()
            if nova_conta not in conta.nomes and nova_conta != '':
                conta.adicionar_conta(nova_conta)
        except NameError:
            pass
    return homepage()


@app.route('/valor-contas', methods=['GET', 'POST'])
def valor_contas():
    if request.method == 'POST':
        try:
            valor_conta = float(request.form['valor_conta'])
            if valor_conta > 0:
                conta.adicionar_valor(valor_conta)
        except ValueError:
            pass
    return homepage()


@app.route('/dividas-divididas')
def dividir_dividas():
    global calculo_individual
    if len(pessoa.nomes) == len(pessoa.rendas) and \
            len(conta.nomes) == len(conta.valores) and \
            len(pessoa.nomes) != 0 and \
            len(conta.nomes) != 0 and \
            not calculo_individual:
        calculo_individual = True
        for n in range(len(pessoa.nomes)):
            familia.adicionar_membros(pessoa.nomes[n], pessoa.rendas[n])
        for n in range(len(conta.nomes)):
            familia.adicionar_conta(conta.nomes[n], conta.valores[n])
    return homepage()


def monetizar(valor):
    return f'{valor:,.2f} R$'


if __name__ == '__main__':
    app.run(debug=True)
