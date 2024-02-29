from decimal import Decimal, getcontext


# Tipos Numéricos

"""
Nesta etapa iremos aprofundar um pouco mais sobre os tipos numéricos em Python
"""

# int()
"""
Este nós já conhecemos, basicamente são números inteiros sem casas decimais 
"""
a = 3

print(a)
print(type(a))

# float()
"""
E este são números de 'ponto flutuante' ou número real, isso por que possuem
casas decimais e por esta razão o tipo que armazena mais informações, lembrando que
pelo fato de Python ser uma linguagem em inglês a divisão dos decimais são 
feitas por '.'(ponto) e não pela ','(vírgula)
"""
b = 2.5

print(b)
print(type(b))

# dir()
"""
Assim como as demais funções Python podemos ver através do dir quais as ferramentas
ou métodos estão agregados as funções 'int()' e 'float()'
"""

dir(int)
dir(float)

"""
Para isso iremos usar o shell (terminal interativo) do Python
"""

# Decimal
"""
Decimal não é uma função built-in, Decimal() é um módulo que precisa der importado no início 
do arquivo, e isso é uma convenção da linguagem apresentada na PEP8 
"""

decimal = Decimal(1) / Decimal(7)
print(decimal)

"""
Agora usaremos o getcontext() para uma maior precisão, para isso estabelecemos a precisão que desejamos 
antes do processo que desejamos executar, como no exemplo abaixo
"""

getcontext().prec = 4
decimal = Decimal(1) / Decimal(7)
print(decimal)


