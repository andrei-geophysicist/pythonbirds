class Pessoa:
    # Atributo de instância e de objetos são criados através do __init__
    def __init__(self, nome = None, idade=49): # atributo de inicialização com o campo default vazio
        self.idade = idade
        self.nome = nome # cria o atributo especial com o parâmetro nome

    def cumprimentar(self): # método(objeto)
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Oliveira')
    print(Pessoa.cumprimentar(p)) # O parâmetro p está explícito
    print(id(p)) # imprime a id do do objeto self
    print(p.cumprimentar()) # O parâmetro p está implícito
    print(p.nome)
    p.nome = 'Andrei'
    print(p.nome)
    print(p.idade)
