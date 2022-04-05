# from DividindoAsDividas.main import adiciona_pessoa
from DividindoAsDividas.pessoa import Pessoa
from DividindoAsDividas.familia import Familia


def test_criando_familia():
    abrantes = Familia('abrantes')
    dantas = Familia('Dantas')

    assert abrantes.nome == 'Abrantes'
    assert abrantes.renda_total == 0
    assert abrantes.pagamentos_mensais == 0

    assert dantas.nome == 'Dantas'
    assert dantas.renda_total == 0
    assert dantas.pagamentos_mensais == 0


def test_criando_pessoa():
    maria = Pessoa('maria', 1000)
    joao = Pessoa('joão', 2000)
    pedro = Pessoa('Pedro', 3000)

    assert maria.nome == 'Maria'
    assert maria.renda == 1000

    assert joao.nome == 'João'
    assert joao.renda == 2000

    assert pedro.nome == 'Pedro'
    assert pedro.renda == 3000


def test_adicionando_membro_da_familia():
    abrantes = Familia('abrantes')
    janio = Pessoa('janio', 1000)
    abrantes.adicionar_membros(janio.nome, janio.renda)

    assert abrantes.membros == {'Janio': 1000}


def test_adicionando_multiplos_membros_da_familia():
    abrantes = Familia('abrantes')

    janio = Pessoa('janio', 1000)
    mariana = Pessoa('mariana', 2000)
    danilo = Pessoa('danilo', 3000)

    abrantes.adicionar_membros(janio.nome, janio.renda)
    abrantes.adicionar_membros(mariana.nome, mariana.renda)
    abrantes.adicionar_membros(danilo.nome, danilo.renda)

    assert abrantes.membros == {'Janio': 1000, 'Mariana': 2000, 'Danilo': 3000}
    assert abrantes.renda_total == 6000


def test_calcular_pagamentos_mensais():
    abrantes = Familia('abrantes')

    assert abrantes.pagamentos_mensais == 0
    abrantes.calcular_pagamentos_mensais(2000)
    assert abrantes.pagamentos_mensais == 2000
    abrantes.calcular_pagamentos_mensais(5000.20)
    assert abrantes.pagamentos_mensais == 7000.20


def test_calcular_pagamento_individual():
    abrantes = Familia('abrantes')

    janio = Pessoa('janio', 1000)
    mariana = Pessoa('mariana', 2000)
    danilo = Pessoa('danilo', 3000)

    abrantes.adicionar_membros(janio.nome, janio.renda)
    abrantes.adicionar_membros(mariana.nome, mariana.renda)
    abrantes.adicionar_membros(danilo.nome, danilo.renda)

    abrantes.calcular_pagamentos_mensais(1500)
    abrantes.calcular_pagamentos_mensais(800)

    soma_pagamentos = 0
    porcentagem_total = 0

    for membro in abrantes.membros.items():
        nome = membro[0]
        renda = membro[1]
        porcentagem_da_renda, pagamento_individual = abrantes.calcular_pagamento_individual(nome, renda)
        print(f'O valor a ser pago por {nome} será de {pagamento_individual:.2f}, '
              f'que equivale a {porcentagem_da_renda*100:.2f}% de todos os pagamentos')

        porcentagem_total += porcentagem_da_renda
        soma_pagamentos += pagamento_individual

    assert (porcentagem_total * 100) == 100
    assert soma_pagamentos == abrantes.pagamentos_mensais
