# Este é um arquivo que terá como objetivo exemplificar alguns dos conceitos mais generalizados da linguagem Python

"""
Python é uma linguagem de programação que atua com o conceito de descrição de uma sentença por linha, como por exemplo:
"""

print("Primeiro programa")

"""
A resposta obtida através da execução deste comando será: Primeiro programa.
Do mesmo modo se eu escrvo o seguinte comando:
"""

1 + 2

"""
Eu terei como resultado o valor 3 como resposta porém, se eu escrever da seguinte forma:
"""

1 
+ 2


"""
Eu terei um erro de identação: IdentantionError
"""

"""
Para executar todos os valore eu preciso utilizar a função print(), a qual serve para imprimir o valor de algo, faço isso da seguinte forma:
"""

print("Primeiro programa")
print(1 + 2)
print(1 + 2 + 5 + 15)

"""
E afinal o que é identação?
Identação em termos gerais significa: 'Espaço no começo de um linha e/ou parágrafo'
E Python usa por convenção 4(quatro) espaços, veremos melhor como funciona posteriormente, mas em programação identação
é utilizada com o intuito de ressaltar a estrutura do algoritmo, aprimorando assim a legibilidade do código
"""

"""
Se quisermos entender um pouco mais sobre o objetivo das funções podemos executar o help() para isso da seguinte forma:
"""

help(print)

"""
A resposta que iremos obter será uma breve explanação sobre o objetivo da função help() no nosso terminal
"""