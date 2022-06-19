"""
Operadores Lógicos:
 * AND, OR, NOT
 * IN e NOT IN
"""

# Comandos and, or e not
a = 2
b = 1
c = 3

if a == b and b < c:
    print("Primeira verificação: Verdade")
else:
    print("Primeira verificação: Mentira")

if a == b or b < c:
    print("Segunda verificação: Verdade")
else:
    print("Segunda verificação: Mentira")

if a == b or not b < c:  # not se aplica da mesma forma que a negação da materia de Lógica para Computação
    print("Terceira verificação: Verdade")
else:
    print("Terceira verificação: Mentira")

# Comandos in e not in
nome = "Samuel"

if "u" in nome:  # not in se aplica da mesma forma
    print(f"Existe a letra U em {nome}.")
else:
    print(f"Não existe a letra U em {nome}.")
