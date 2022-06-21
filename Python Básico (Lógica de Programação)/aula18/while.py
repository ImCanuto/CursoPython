"""
Estruturas de repetição:
 * While
"""
"""
x = 0
while x <= 5:
    if x == 3:
        x += 1  # Iteração para o programa não ficar "preso" no 3
        continue  # Função para pular para o próximo ciclo do laço, nessa caso, pulando o número 3 na contagem
    print(x)
    x += 1
"""
# Exemplo com estruturas aninhadas:
"""
a = 0  # coluna
b = 0  # linha

while a <= 5:
    b = 0
    while b <= 5:
        print(f"({a},{b})")
        b += 1
    a += 1
"""
# Construindo uma calculadora simples

while True:
    print()
    num_1 = input("Digite um número inteiro ou [s] para sair: ")

    if num_1 == "s":
        break

    num_2 = input("Digite outro número: ")

    if not num_1.isnumeric() or not num_2.isnumeric():
        print("Você precisa digitar números inteiros.")
        continue

    operador = input("Digite o operador (+, -, / ou *): ")

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == "+":
        print(f"{num_1} + {num_2} = {num_1 + num_2}")
    elif operador == "-":
        print(f"{num_1} - {num_2} = {num_1 - num_2}")
    elif operador == "/":
        print(f"{num_1} / {num_2} = {num_1 / num_2}")
    elif operador == "*":
        print(f"{num_1} * {num_2} = {num_1 * num_2}")
    else:
        print("Digite um operador válido.")
        continue
