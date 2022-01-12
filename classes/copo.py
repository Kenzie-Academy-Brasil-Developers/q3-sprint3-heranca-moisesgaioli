from classes.recipiente import Recipiente


class Copo(Recipiente):
    def __init__(self, tamanho=0, conteudo=0, limpo=True) -> None:
        super().__init__(tamanho=tamanho, conteudo=conteudo, limpo=limpo)

        self.tamanho = tamanho
    
    def encher(self, bebida = 'água'):
        if self.limpo == False:
            return 'Não se pode encher um copo sujo'
        else:
            self.sujar()
            self.conteudo = self.tamanho
            self.bebida = bebida
    
    def beber(self, quantidade):
        if quantidade < 0:
            return 'Quantidade deve ser positiva'
        if quantidade > self.conteudo:
            return 'Não há bebida suficiente no copo'
        self.conteudo -= quantidade
    
    def lavar(self):
        self.bebida = None
        self.conteudo = 0
        self.limpo = True
    
    def __repr__(self) -> str:
        if self.conteudo == 0:
            return 'Um copo vazio de %sml' % (self.tamanho)
        else:
            return 'Um copo de %sml contendo %sml de %s' % (self.tamanho, self.conteudo, self.bebida)
    
    def __str__(self) -> str:
        if self.conteudo == 0:
            return f'Um copo vazio de {self.tamanho}'
        else:
            return f'Um copo de {self.tamanho}ml contendo {self.conteudo}ml de {self.bebida}'




    




