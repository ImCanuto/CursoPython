nome = 'Samuel'
idade = 22
altura = 1.84
maior_de_idade = 22 >= 18
peso = 75
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos e seu IMC é:', imc)
# Utilizando a formatação de strings "f" temos:
print(f'{nome} tem {idade} anos e seu IMC é: {imc:.2f}')
print('{} tem {} anos e seu IMC é: {:.2f}'.format(nome, idade, imc))
# Também é possivel definir {0, 1, 2, etc} para repetir os parametros
