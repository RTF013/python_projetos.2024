faturamento = 1000
custo = 700
lucro = 300

margem = lucro / faturamento
print(f"faturamento: R${faturamento:,.2f}\n Custo: {custo}\n Lucro: {lucro}")
print(f'Margem: {margem:.1%}')

#exercios descobrir o e-mail de uma pessoa
nome = "João Paulo Lira"
email = "emailfalso2@gmail.com"
posicao = email.find('@')
print(posicao)
servidor = email[posicao:]
print(servidor)

#pegar o primeiro nome do usuario
posicao = nome.find(" ")
primeiro_nome = nome[:posicao]
print(primeiro_nome)

#contrua uma mensagem: Usuario primeiro_nome cadastrado com sucesso com o e-mail: tal
mensagem = f"Usuario {primeiro_nome} cadastrado com sucesso com o email: {email}"
print(mensagem)

#contrua uma mensagem: Enviamos um link de confirmação para o email:
primeira_letra = email[0]
print(primeira_letra)
mensagem2 = f"Enviamos um link de confirmação para o e-mail {primeira_letra}***{servidor}"
print(mensagem2)
