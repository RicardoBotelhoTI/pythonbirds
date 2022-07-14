class Pessoa: # nome de classe tem que começar com letra maiscula se for mais de uma palavra a posteior também começa com letra maiscula ex: class PessoaCadastro:
    def __init__(self, nome=None, idade=41):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Luciano')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar()) # Passando o elemento depois o metodo
    print(p.nome)
    p.nome = 'Ricardo'
    print(p.nome)