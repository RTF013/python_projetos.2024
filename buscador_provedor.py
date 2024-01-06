def extrair_provedor(email):
    # Dividir o endereço de e-mail no caractere '@'
    partes = email.split('@')

    # Verificar se há pelo menos duas partes (nome do usuário e domínio)
    if len(partes) >= 2:
        # A segunda parte é o domínio, que é o provedor de e-mail
        provedor = partes[1]
        return provedor
    else:
        raise ValueError("Endereço de e-mail inválido")

# Exemplo de uso
endereco_email = "roosevelt@slttransporte.com"
provedor_email = extrair_provedor(endereco_email)
print(f"Provedor de e-mail: {provedor_email}")
