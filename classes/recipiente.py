class Recipiente:

    def __init__(self, tamanho = 0, conteudo = 0, limpo = True) -> None:
        if tamanho < 0:
            self.tamanho = 0
        else:
            self.tamanho = tamanho

        self.conteudo = conteudo
        self.limpo = limpo

    def esvaziar(self):
        self.conteudo = 0
    
    def esta_vazio(self):
        if self.conteudo > 0:
            return True 
        else:
            return False
        
    def lavar(self):
        self.conteudo = 0
        self.limpo = True

    def esta_limpo(self):
        if self.limpo == True:
            return True
        else:
            return False
    
    def estado(self):
        if self.limpo == True:
            return 'limpo'
        else:
            return 'sujo'
    
    def sujar(self):
        self.limpo = False

    def __repr__(self) -> str:
        return 'Um recipiente %s não especificado.' % (self.estado())
    
    def __str__(self) -> str:
        return f'Um recipiente {self.estado()} não especificado.'

