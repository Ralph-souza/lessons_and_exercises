# Listas

"""
Nesta etapa iremos aprofundar ainda mais no que são as listas
e como podemos manipular as mesmas. Listas são um conjunto de 
elementos indexados, listas são mutáveis e por esta razão podem sofrer 
acréscimo ou decréscimo de valores dinamicamente. A mesma é representada 
pela utilização de colchetes '[]' 
"""

new_list = [] # Cuidado ao nomear listas de 'list', visto que 'list' é um método built-in

print(len(new_list))

new_list.append(1)
new_list.append(5)

print(new_list)
print(len(new_list))

new_list.append('Ana')
new_list.append('João')

print(new_list)
print(len(new_list))

"""
No exemplo acima temos uma lista a princípio vazia que recebeu novos dados
por meio de adição através da utilização do método append(), porém apesar de Python
permitir essa mescla de informações isso não quer dizer que devemos fazer na 
prática, o ideal seria que uma lista armazenasse um tipo de dado, fosse ele
tipo string ou numérico, esse processo permite até mesmo a inclusão de uma 
nova lista dentro da lista existentes
"""

new_list.remove(5)

print(new_list)
print(len(new_list))

"""
Podemos remover um elemento específico ao utilizarmos o método remove() como no exemplo acima
"""

new_list.reverse()

print(new_list)

"""
Podemos inverter os valores da lista ao utilizarmos o método reverse()
"""

new_list.pop()

print(new_list)
print(len(new_list))

"""
Ao utilizarmos o método pop() apagamos sempre o último elemento da lista
"""

defined_list = [1 , 5, 'Manoel', 'Lindalva', 3.1415]

print(defined_list.index('Lindalva'))

"""
Podemos usar o index para encontrarmos o índice de um elemento na lista
"""

print(defined_list[3])

"""
Do mesmo modo podemos descobrir o elemento pelo índice como no exemplo acima
"""

print(defined_list[-1])

"""
Se quisermos o último elemento da lista basta usarmos a indexação negativa '[-1]'
"""

print(1 in defined_list)
print('Manoel' in defined_list)
print('Ralph' not in defined_list)
print('Larissa' in defined_list)

"""
Podemos utilizar o operador 'in' e 'not' para verificarmos se um item pertence a uma lista como vimos acima
"""

names_list = ['Lindalva', 'Manoel', 'Robson', 'Wanessa', 'Ralph']

print(names_list[1:3])

"""
No exemplo acima pegamos os elementos da lista a partir do índice [1] até o [3] lembrando que, assim como foi
com as strings o índice [3] não será apresentado
"""

print(names_list[1:-1])

"""
Neste exemplo ele irá até o fim a partir do índice [1] sem incluir o [-1] que seria o último
"""

print(names_list[::2])

"""
Já no exemplo acima estamos definido que será percorrida a lista toda porém de 2(dois) em 2(dois)
"""

print(names_list[::-1])

"""
Acima invertemos a lista
"""
