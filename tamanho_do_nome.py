# Solicita ao usuário para digitar o primeiro nome
nome = input("Digite seu primeiro nome: ")

# Obtém o comprimento do nome
comprimento_nome = len(nome)

# Determina a mensagem com base no comprimento do nome
if 1 <= comprimento_nome <= 6:
    mensagem = "Seu nome é pequeno."
elif 6 < comprimento_nome <= 8:
    mensagem = "Seu nome é normal."
elif 8 < comprimento_nome <= 12:
    mensagem = "Seu nome é grande."
else:
    mensagem = "Seu nome é muito grande ou muito curto."

# Exibe a mensagem
print(mensagem)
