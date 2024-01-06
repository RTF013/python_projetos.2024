class Usuario:
    def __init__(self, nome, idade, sobrenome):
        self.nome = nome
        self.idade = idade
        self.sobrenome = sobrenome

idade = 1
continuar = 1
lista_usuario = []
while continuar != 0:
    nome = input('Digite o seu nome: ')
    idade = int(input('Digite sua idade: '))
    sobrenome = input('Digite seu sobrenome: ')
    usuario = Usuario(nome, idade, sobrenome)

    lista_usuario.append(usuario)

    if usuario.idade == 99:
        break
    if usuario.idade == 98:
        continue

    print(f'Olá, {usuario.nome} {usuario.sobrenome}, sua idade é {usuario.idade}')

    if usuario.idade <= 17:
        print(f'{usuario.nome} é adolescente')
    elif usuario.idade >= 18 and usuario.idade <= 50:
        print(f'{usuario.nome} é adulto')
    else:
        print(f'{usuario.nome} é idoso')

    continuar = int(input('Deseja continuar cadastrando? 0 - sair 1 - continuar'))

else:
        print('Lista de usuários cadastrados')

        for x in lista_usuario:
            print(f'Nome completo: {x.nome} {x.sobrenome} - idade {x.idade}')

        print('o loop entrou no else')





