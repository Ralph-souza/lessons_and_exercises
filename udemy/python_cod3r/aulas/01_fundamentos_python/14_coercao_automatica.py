# Coerção Automática

"""
Aqui nós iremos ver como exemplos de quando o Python pode fazer
uma coerção automática, em casos onde não há ambiguidades.
"""

print(10 / 2)
print(type(10 / 2))

print(10 / 3)

print(10 // 3)
print(type(10 // 3))

print(10 // 3.3)
print(type(10 // 3.3))

print(10 / 2.5)

print(2 + True) # Neste caso Python assume que TRUE é igual a 1
print(2 + False) # Neste caso ele assume que FALSE é igual a 0
