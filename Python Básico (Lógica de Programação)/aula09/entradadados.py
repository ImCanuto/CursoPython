"""
Entrada de Dados:
"""

"""
nome_usuario = input("Qual é o seu nome? ")  # Comando que registra a entrada do usuário e retorna como str
idade = input("Quantos anos você tem? ")
ano_nascimento = 2022 - int(idade)  # Casting de str para int

print(f"O nome do usuário é {nome_usuario}, ele tem {idade} anos e nasceu em {ano_nascimento}.")
"""

#  Exercício: Calculadora

num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))
soma = num_1 + num_2
sub = num_1 - num_2
multi = num_1 * num_2
div = num_1 / num_2

print(f"A soma entre {num_1} e {num_2} é: {soma}")
print(f"A subtração entre {num_1} e {num_2} é: {sub}")
print(f"A multiplicação entre {num_1} e {num_2} é: {multi}")
print(f"A divisão entre {num_1} e {num_2} é: {div:.2f}")
