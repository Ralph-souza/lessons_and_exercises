# Operadores Lógicos

"""
A semântica (significado) destes operadores é semelhante ao seu significado em inglês, são eles: 

AND
OR
NOT

Fazendo assim a verificação da veracidade entre os operandos, nos exemplos abaixo veremos isso 
acontecendo de forma binária, ou seja, com uso de dois operandos.
"""

# Tabela verdade

"""
A tabela verdade apresenta as regras de verficiação com base no operador lógico.
"""

# Tabela Verdade AND

print(True and True)
print(True and False)
print(False and True)
print(False and False)

"""
Neste caso teremos como resposta para as operações:

True
False
False
False

Somente quando as duas condições são satisfeitas teremos True.
Podemos ver mais um exemplo onde temos algumas condições verdadeiras e apenas
uma falsa fazendo com que o retorno da operação seja False
"""
print(True and True and True and False and True and True and True and True)

# Tabela Verdade OR 

print(True or True)
print(True or False)
print(False or True)
print(False or False)

"""
Neste caso teremos como resposta para as operações:

True
True
True
False

Neste caso desde de que uma das condições seja satisfeita teremos como resultado True,
também podemos ver com isso acontece com o seguinte exemplo onde temos algumas
condições falsas e apenas uma verdadeira e o retorno da operação é True
"""
print(False or False or True or False or False or False or False or False)

# Tabela Verdade NOT

"""
Já o operador NOT não possui necessariamente uma tabela verdade, visto que o mesmo serve
para inverter os valores booleanos, ou seja, se o valor for TRUE o NOT retornará FALSE 
se for FALSE o mesmo retornará o valor TRUE

NOT TRUE  -> False
NOT FALSE -> True

Assim sendo o único operador UNÁRIO neste processo
"""

# Tabela Verdade XOR

"""
Esta expressão pode ser lida como OU EXLUSIVO, e como diz este operador avalia os 
operandos e valida a exclusividade das condições como sendo UMA ou OUTRA
"""

print(True != True)
print(True != False)
print(False != True)
print(False != False)

"""
Neste caso teremos como resposta para as operações:

False
True
True
False

Neste caso, para simplificar a leitura podemos ler as expressões como
TRUE diferente(!=) de False
"""

# Operadores Bit-a-Bit(Bitewise)

"""
Antes de mais nada são exemplos de operadores BIT A BIT:

& -> AND
| -> OR
^ -> XOR

Apesar de possuírem uma certa similaridade com os operadores acima na execução os 
operadores lógico BIT-A-BIT fazem uma comparação dos bits do primeiro operando
com os bits do segundo, se ambos os bits forem 1, o bit de resultado correspondente 
será definido como 1. Caso contrário, o bit de resultado correspondente é 
definido como 0.
Somente utilizamos operadores bitwise quando precisamos realizar operações de nível
de bits com números inteiros, ou seja, em representações binárias, por exemplo:
"""
a = 5 # Em binário: 0101
b = 3 # Em binário: 0011

result = a & b
# Em binário o resultado será 0001 (1 em decimal)

print(f"Resultado da operação AND em BITWISE: {result}")

"""
Após comparar BIT A BIT em ambos ele transformou àqueles que não eram correspondentes
em 0 e trouxe o correspondente como 1
"""