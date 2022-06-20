"""
Condicionais:
* IF, ELIF e ELSE
"""

nome = "Samuel"
idade = int(input("Idade: "))
idade_maior = 30
idade_menor = 20

if idade_menor <= idade <= idade_maior:
    print(f"{nome} pode pegar o empréstimo.")
else:
    print(f"{nome} NÃO pode pegar o empréstimo!")
