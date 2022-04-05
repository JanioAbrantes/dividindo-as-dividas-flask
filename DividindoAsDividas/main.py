from pessoa import Pessoa
from familia import Familia

nome_familia = input('Insira o nome de sua família: ')
grupo_familiar = Familia(nome_familia)

while True:
    nome_pessoa = input('Digite o nome que deseja adicionar a familia, ou deixe em branco caso não queira '
                        'adicionar mais ninguém: ')
    if nome_pessoa == '':
        break

    while True:
        try:
            renda_pessoa = float(input('Digite a renda mensal dessa pessoa: '))
            break
        except ValueError:
            print('Por favor, informe um valor válido.')

    nova_pessoa = Pessoa(nome_pessoa, renda_pessoa)
    grupo_familiar.adicionar_membros(nova_pessoa.nome, nova_pessoa.renda)
    print(nova_pessoa)

while True:
    try:
        novo_pagamento = float(input('Digite o valor a ser pago, ou digite 0 caso não'
                                    ' queira adicionar mais nenhum valor: '))
        if novo_pagamento == 0:
            break
        grupo_familiar.calcular_pagamentos_mensais(novo_pagamento)
    except ValueError:
        print('Por favor, informe um valor válido.')

for membro in grupo_familiar.membros.items():
    nome_membro = membro[0]
    renda_membro = membro[1]
    porcentagem_da_renda, pagamento_individual = \
        grupo_familiar.calcular_pagamento_individual(nome_membro, renda_membro)
    print(f'O valor a ser pago por {nome_membro} será de R${pagamento_individual:.2f}, '
          f'que equivale a {porcentagem_da_renda * 100:.2f}% de todos os pagamentos')
