class Pessoa: # nome de classe tem que começar com letra maiscula se for mais de uma palavra a posteior também começa com letra maiscula ex: class PessoaCadastro:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(renzo, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar()) # Passando o elemento depois o metodo
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramanho'
    del luciano.filhos
    print(luciano.__dict__)
    print(renzo.__dict__)