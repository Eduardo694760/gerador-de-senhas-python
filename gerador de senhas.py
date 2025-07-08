print("Desenvolvido por Eduardo José")

# -------------------------------
# Gerador de Senhas Fortes
# Autor: Eduardo José Jorge S.
# Linguagem: Python 3
# -------------------------------

import random
import string

def gerar_senha(tamanho=12, usar_maiusculas=True, usar_numeros=True, usar_simbolos=True):
    letras_minusculas = string.ascii_lowercase
    letras_maiusculas = string.ascii_uppercase if usar_maiusculas else ''
    numeros = string.digits if usar_numeros else ''
    simbolos = string.punctuation if usar_simbolos else ''

    
    caracteres = letras_minusculas + letras_maiusculas + numeros + simbolos

    if not caracteres:
        return "Erro: Nenhum tipo de caractere foi selecionado."

    senha = []

    if usar_maiusculas:
        senha.append(random.choice(letras_maiusculas))
    if usar_numeros:
        senha.append(random.choice(numeros))
    if usar_simbolos:
        senha.append(random.choice(simbolos))

    while len(senha) < tamanho:
        senha.append(random.choice(caracteres))

    random.shuffle(senha)

    return ''.join(senha)

# -------------------------------
# Execução do programa
# -------------------------------
if __name__ == "__main__":
    print("------ Gerador de Senhas Fortes ------")
    
    try:
        tamanho = int(input("Digite o tamanho da senha (mínimo recomendado: 8): "))
        usar_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
        usar_numeros = input("Incluir números? (s/n): ").lower() == 's'
        usar_simbolos = input("Incluir símbolos (!@#$...) ? (s/n): ").lower() == 's'

        senha_gerada = gerar_senha(
            tamanho=tamanho,
            usar_maiusculas=usar_maiusculas,
            usar_numeros=usar_numeros,
            usar_simbolos=usar_simbolos
        )

        print("\nSenha gerada:")
        print(senha_gerada)
    except ValueError:
        print("Erro: Digite apenas números válidos para o tamanho da senha.")