"""
Manipulando Strings:
 * String indices
 * Fatiamento de strings [inicio:fim:passo]
 * Funções built-in len, abs, type, print, etc...
"""

# indices positivos  [012345678]
texto              = "Python S2"
# indices negativos -[987654321]

print(texto[2])  # Mostrará o indice 2 ("t")
print(texto[-1])  # Mostrará o indice -1 ("2")
# Creio que, assim como em C, isso se dá pois as strings são vetores
# Mas isso não foi dito na aula, foi devaneio da minha cabeça mesmo

# Fatiamento de string
novo_texto = texto[3:6]  # Mostrando do indice 3 ao 6 (último indice não é mostrado)

print(novo_texto)
print(texto[:-2])  # Mostrando do começo da string até o indice -2
print(texto[0:6:2])  # Mostrando do indice 0 ao 6, "pulando" de 2 em 2 (passo)
