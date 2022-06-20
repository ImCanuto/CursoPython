"""
String Methods:
 * Funções para evitar que o usuário quebre o código digitando o que não devia
 * isnumeric, isdigit e isdecimal
"""

"""
num_1 = input("Digite um número: ")
num_2 = input("Digite outro número: ")

if num_1.isdigit() and num_2.isdigit():  # Isso ainda não impede que dê problema com floats
    num_1 = int(num_1)
    num_2 = int(num_2)

else:
    print("Digite um valor válido!")

soma = num_1 + num_2
sub = num_1 - num_2
multi = num_1 * num_2
div = num_1 / num_2

print(f"A soma entre {num_1} e {num_2} é: {soma}")
print(f"A subtração entre {num_1} e {num_2} é: {sub}")
print(f"A multiplicação entre {num_1} e {num_2} é: {multi}")
print(f"A divisão entre {num_1} e {num_2} é: {div:.2f}")

"""

# ############################### Solução dada pelo professor: ############################### #

import re


def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)


num_1 = input("Digite um número: ")
num_2 = input("Digite outro número: ")

if is_number(num_1) and is_number(num_2):
    num_1 = float(num_1)
    num_2 = float(num_2)
    soma = num_1 + num_2
    sub = num_1 - num_2
    multi = num_1 * num_2
    div = num_1 / num_2

    print(f"A soma entre {num_1} e {num_2} é: {soma:.2f}")
    print(f"A subtração entre {num_1} e {num_2} é: {sub:.2f}")
    print(f"A multiplicação entre {num_1} e {num_2} é: {multi:.2f}")
    print(f"A divisão entre {num_1} e {num_2} é: {div:.2f}")

else:
    print("Digite um valor válido!")

# No lugar de if e else também foi sugerido a utilização de try e except, que serão explicados futuramente