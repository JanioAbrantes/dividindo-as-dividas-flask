class Pessoas:
    """
    Classe que irá criar o objeto pessoa, pegando o nome e a renda dela.
    """
    def __init__(self):
        """
        Cria um novo grupo de pessoa.
        :param nome: str
        :param renda: float
        """
        self.nomes = ()
        self.rendas = ()

    def adicionar_nome(self, nome:str):
        """
        Adiciona o nome de uma pessoa
        :param nome: str
        :return: None
        """
        self.nomes = (self.nomes + (nome,))

    def adicionar_renda(self, renda:float):
        """
        Adiciona a renda de uma pessoa
        :param renda: float
        :return: None
        """
        self.rendas = (self.rendas + (renda,))
