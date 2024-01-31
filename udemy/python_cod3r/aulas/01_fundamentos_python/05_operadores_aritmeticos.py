# Operadores Aritméticos 

# Operadores Binários

"""
Vamos começar mostrando os operadores binários, ou seja, que precisam de 2(dois) operandos para executar sua função
"""

# Soma
print(1 + 2)

# Subtração
print(4 - 7)

# Multiplicação
print(2 * 5.3) # Aqui nós temos dois tipos distintos de dados sendo eles do tipo inteiro(int) e do tipo ponto flutuante(float)

"""
No caso acima o resultado será em ponto flutuante(float) por ser o que mais armazena informação entre os dois tipos
"""

# Divisão
print(9.4 / 3) # Aqui nós teremos um resultado equivalente a 3.13333

"""
Porém eu posso fazer com que saia um resultado obrigatoriamente inteiro utilizando a barra dupla como no exemplo abaixo
"""
# Divisão inteira
print(9.4 // 3)

# Exponenciação
print(2 ** 8)

# Módulo (Resto da Divisão)
print(10 % 3)

"""
Neste caso se dividirmos 10(dez) por 3(três) teremos como resultado o valor 3(três) e o resto da divisão será 1(um)
"""

# Podemos atribuir valores a variáveis e executar a operação que desejarmos por meio das mesmas, como no exemplo abaixo

a = 12
b = a # Neste caso B terá o mesmo valor de A

print(a + b)

"""
Vale esclarecer que o operador entre os dois operandos, neste exemplo o '+', recebe o nome de INFIX e isso serve para todos operadores entre dois operandos
"""

# Operadores Unários

"""
Operadores unários são àqueles que precisam apenas de um operando, como no exemplo abaixo
"""

a = 12 
a += 1
print(a)

"""
Neste exemplo A teria o valor de 12(doze), o operador unário '+=' é o que chamados de operador de ATRIBUÍÇÃO-ADIÇÃO, ou seja, que vem antes do operando A
e neste caso ele acrescenta mais 1(um) ao valor de A obtendo assim como resposta o valor 13(treze), e temos também o operador ATRIBUÍÇÃO-SUBTRAÇÃO que vem
antes do operando como no exemplo abaixo, e neste caso fazendo o decréscimo de -1(menos um) ao valor do operando A recebendo assim o valor
de 11(onze) como retorno
"""

a = 12 
a -= 1
print(a)
