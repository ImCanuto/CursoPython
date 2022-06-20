"""
Formatando valores com modificadores

 * :s - strings
 * :d - inteiros
 * :f - float
 * :.(número)f - Quantidades de casas decimais de um float Ex: :.2f
 * :(caractere)(>, <, ou ^)(quantidade)(s, d ou f) Ex: 0>10 (completará com zeros à direita até completar 10 caracteres)

 > - Esquerda
 < - Direita
 ^ - Centro
"""

num1 = 158
num2 = 24

print(f"{num1 / num2:.2f}")
print(f"{num1:0>10}")
print(f"{num2:0^10}")
print(f"{num1 + num2:0<10}")

nome = "Samuel"
sobrenome = "Canuto"

print(f"{nome:@^30}")
print("Meu nome é {} {}".format(nome, sobrenome))
# ou
print("Meu nome é {n} {s}".format(s=sobrenome, n=nome))  # Vantagem: Repetir a variável em vários ordens diferentes
