"""
Tipos de dados:

str - string (textos 'assim' "assim")
int - inteiro (1234 0 -10 30 etc)
float - real/ponto flutuante (10.5 3.2 7.32 etc)
bool - booleano (True/False)
"""

print('Pimba', type('Pimba'))  # Mostra a classe do objeto ("tipo")
print(10, type(10))
print(3.5, type(3.5))
print(3 == 3, type(3 == 3))
print('L' == 'J', type('L' == 'J'))

print('Pimba', type('Pimba'), bool('Pimba'))  # Conversão de tipos
print(10, type(10), float(10))  # Type convert

"""
Exercício: Criar um "cadastro" e exibir na tela
"""

# Nome: string
print('Samuel', type('Samuel'))

# Idade: int
print(22, type(22))

# Altura: float
print(1.84, type(1.84))

# É maior de idade: bool
print(22 > 18, type(22 > 18))
