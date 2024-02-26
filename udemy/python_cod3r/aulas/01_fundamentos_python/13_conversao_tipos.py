# Conversão de Tipos

"""
Nesta etapa iremos ver como podemos fazer a conversão de certos tipos
seguindo algumas regras básicas visto que o Python precisa que o processo
solicitado seja explícito, por assim, para ser processado.
"""

print(2 + 3)
print('2' + '3') # Concatenação

a = 2
b = '3'

print(type(a))
print(type(b))

print(a + int(b))
print(str(a) + b)

"""
Quando falamos de regras queremos dizer o seguinte, se A fosse
3.5 ao invés de 3 e tentassemos converter para inteiro não daria certo
um erro seria apresentado porém quando usamos float... 
"""

a = 2
b = '3.5'

print(a + float(b))

"""
Assim sendo antes de tentarmos converter um valor precisamos nos certificar de 
que o mesmo corresponde a um padrão que permita ser convertido
"""
