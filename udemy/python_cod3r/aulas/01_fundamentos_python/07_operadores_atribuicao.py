# Operadores de Atribuíção

"""
Nesta etapa veremos os operadores de atribuíção, tais como:

=   -> ATRIBUÍÇÃO e/ou RECEBE
+=  -> ATRIBUÍÇÃO DE ADIÇÃO
-=  -> ATRIBUÍÇÃO DE SUBTRAÇÃO
*=  -> ATRIBUÍÇÃO DE MULTIPLICAÇÃO
/=  -> ATRIBUÍÇÃO DE DIVISÃO
%=  -> ATRIBUÍÇÃO DE MÓDULO
**= -> ATRIBUÍÇÃO DE EXPONENCIAÇÃO
//= -> ATRIBUÍÇÃO POR INTEIRO

Vejamos os exemplos abaixo:
"""

a = 13 # A variável A RECEBE o valor inteiro 13(treze)
a = a + 7 # A variável A agora RECEBE mais 7(sete) somado ao valor anterior de A tendo como resultado 20(vinte)
print(a)

a += 5 # Esta atribuíção funcionaria do mesmo modo se eu escrevesse A = A + 5
print(a)    

a -= 3
print(a) # Aqui estou pegando o valor de A e SUBTRAINDO 3(três) sendo o mesmo que A = A - 3

"""
Os demais exemplos abaixo seguirão esta mesma ideia de desenvolvimento de acordo com seus operadores aritméticos
"""

a *= 2
print(a)

a /= 4
print(a)

a %= 4
print(a)

a **= 8
print(a)

a //= 256
print(a)

"""
Executando o código com esses exatamente desta forma teremos como resposta os seguintes valores:

20
25
22
44
11.0
3.0
6561.0
25.0
"""
