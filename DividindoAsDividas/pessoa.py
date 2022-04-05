from DividindoAsDividas.familia import Familia
class Pessoa:
    """
    Classe que irá criar o objeto pessoa, pegando o nome e a renda dela.
    """

    def __init__(self, nome:str, renda:float):
        """
        Cria uma nova pessoa.
        :param nome: str
        :param renda: float
        """
        self.nome = nome.capitalize()
        self.renda = renda

    def __repr__(self):
        """
        Representa a pessoa, informando seu nome e sua renda.
        :return: str
        """
        return f'Nome: {self.nome} Renda: {self.renda}'
