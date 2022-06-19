"""
Desafio:
* Criar variáveis para nome, idade, altura e peso
* Criar variável com o ano atual
* Obter o ano de nascimento da pessoa (baseado na idade e ano atual)
* Obter o IMC da pessoa com 2 casas decimais
* Exibir tudo na tela utilizando F-Strings
"""

nome = 'Samuel'
idade = 22
altura = 1.84
peso = 75
ano_atual = 2022
ano_nascimento = ano_atual - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é: {imc:.2f}.')
print(f'{nome} nasceu em {ano_nascimento}.')
