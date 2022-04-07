class Familia:
    """
    Classe criada para juntar as pessoas em um dicionário, onde o nome será a chave e a renda o valor
    Também será responsável por somar a renda total de todas as pessoas registradas, assim como o pagamento
    total a ser dividido e a parcela que cada um pagará.
    """

    def __init__(self, nome:str):
        """
        Cria uma nova família, com o nome informado
        :param nome: str
        """
        self.renda_total = 0
        self.pagamentos_mensais = 0
        self.nome = nome.capitalize()
        self.membros = {}
        self.contas_a_pagar = {}

    def adicionar_membros(self, nome:str, renda:float):
        """
        Adiciona uma pessoa a classe família
        :param nome: str
        :param renda: float
        :return: None
        """
        self.membros[nome] = renda  # Cria uma chave e um valor utilizando nome e renda da pessoa
        self.renda_total += renda  # Adiciona a renda da pessoa à renda total da familia

    def calcular_pagamentos_mensais(self, nome_conta:str, valor_a_pagar:float):
        """
        Calcula a soma de todos os pagamentos informados, um de cada vez
        :param nome_conta: str
        :param valor_a_pagar: float
        :return: None
        """
        self.contas_a_pagar[nome_conta] = valor_a_pagar
        self.pagamentos_mensais += valor_a_pagar

    def calcular_pagamento_individual(self, membro:str, renda:float):
        """
        Calcula quanto cada pessoa deverá pagar, proporcionalmente a sua renda de acordo com a renda total.
        :param membro: str
        :param renda: float
        :return: float
        """
        porcentagem_da_renda = renda/self.renda_total  # Calcula a porcentagem que deverá ser pago pelo membro
        pagamento_individual = self.pagamentos_mensais * porcentagem_da_renda  # Calcula o valor a ser pago
        return f'O valor a ser pago por {membro} será de: {pagamento_individual:.2f}'

    def __repr__(self):
        """
        Informa o nome, a renda total e os pagamentos mensais da familia.
        :return: str
        """
        return f'Família: {self.nome}\nRenda Total: {self.renda_total}\nPagamentos Mensais: {self.pagamentos_mensais}'
