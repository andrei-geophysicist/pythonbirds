class Pessoa:
    def cumprimentar(self): # método(objeto)
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p)) # O parâmetro p está explícito
    print(id(p)) # imprime a id do do objeto self
    print(p.cumprimentar()) # O parâmetro p está implícito