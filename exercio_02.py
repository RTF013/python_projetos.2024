# Solicita ao usuário para digitar a hora, e conforme ele digitar o horario informar saudação e hora.
hora = int(input("Digite a hora: "))

# Verifica a saudação apropriada com base na hora
if 0 <= hora < 12:
    saudacao = "Bom dia"
elif 12 <= hora < 18:
    saudacao = "Boa tarde"
else:
    saudacao = "Boa noite"

# Exibe a saudação
print(f"{saudacao}! A hora é {hora} horas.")
