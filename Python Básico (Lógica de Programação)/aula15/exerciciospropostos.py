"""
1) Faça um programa que peça ao usuário um número inteiro,
informe se esse número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
2) Faça um programa que peça a hora ao usuário e, baseado no horário descrito,
exiba a saudação apropriada. Ex: Bom dia! (0-11), Boa tarde! (12-17) e Boa noite! (18-23)
"""

"""
3) Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto."; se tiver de 5 a 6 letras escreva "Seu nome é normal.";
se for maior que 6 escreva "Seu nome é grande."
"""


# Exercício 1
"""
num = input("Digite um número inteiro: ")

if num.isdigit():
    num = int(num)

    if num % 2 == 0:
        print(f"{num} é par.")
    else:
        print(f"{num} é impar.")

else:
    print(f'{num} não é um número inteiro.')
"""

# Exercício 2
"""
hora = input("Digite a hora atual, sem os minutos (de 0 à 23): ")

if hora.isdigit():
    hora = int(hora)

    if 0 <= hora <= 23:
        if hora <= 11:
            print("Bom dia!")
        elif hora <= 17:
            print("Boa tarde!")
        else:
            print("Boa noite!")

    else:
        print("Horário deve ser de 0 a 23.")

else:
    print("Digite um horário válido.")
"""

# Exercício 3

nome = input("Digite seu primeiro nome: ")
qtd_nome = len(nome)

if qtd_nome <= 4:
    print(f"{nome}, seu nome é curto.")
elif qtd_nome <= 6:
    print(f"{nome}, seu nome é normal.")
else:
    print(f"{nome}, seu nome é grande.")
