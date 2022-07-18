class Contas:

    def __init__(self):
        self.nomes = ()
        self.valores = ()

    def adicionar_conta(self, nome_conta:str):
        self.nomes = (self.nomes + (nome_conta,))

    def adicionar_valor(self, valor_conta:float):
        self.valores = (self.valores + (valor_conta,))
