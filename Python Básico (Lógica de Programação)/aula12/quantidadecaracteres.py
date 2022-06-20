"""
Quantidade de caracteres:
* Comando len
"""

# Não funciona com tipos numéricos
# Os espaços também são contados
# Saída como int, não sendo necessário Type Casting

usuario = input("Digite seu usuário: ")
qtd_caracteres = len(usuario)
qtd_max = 5

print(f"{usuario}, {qtd_caracteres} caracteres.")

if qtd_caracteres > qtd_max:
    print(f"{usuario} excede a quantidade máxima de caracteres.")
else:
    print(f"{usuario} não excede a quantidade máxima de caracteres.")
