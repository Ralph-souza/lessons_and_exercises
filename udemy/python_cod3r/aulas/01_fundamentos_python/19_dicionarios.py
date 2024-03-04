# Dicionários

"""
Dicionários são estruturas que contêm chave e valor, sendo representado
pelo uso de chaves '{}', além disso possuímos neste caso uma síntaxe 
específica para construção constituída de {'chave': valor,}, por via de 
regra a chave é sempre uma string, em alguns casos pode ser diferente mas
o mais comum de nos depararmos são strings
"""

person = {
    'name': 'Ralph Santos Souza',
    'age': 39,
    'courses': [
        'Inglês', 
        'Francês'
    ]
}

print(type(person))
print(person['name'])
print(person['age'])
print(person['courses'])

"""
Ao utilizarmos o dicionário podemos acessar cada um dos valores pelas suas 
respectivas chaves como vemos no exemplo acima
"""

print(person['courses'][0])

"""
Do mesmo modo uma que chamamos a chave e esta vem a ser um lista podemos acessar um
elemento específico através do seu índice, com vemos no exemplo acima
"""

print(person.keys())
print(person.values())
print(person.items())

"""
Também é possível acessarmos as chaves, valores ou os items que compõem nosso
dicionário da seguinte forma
"""

print(person.get('name'))

"""
Também podemos usar o método GET para pegarmos um elemento específico em nosso dicionário
"""

print(person.get('relatives', []))

"""
No exemplo acima podemos ver que através da utilização do método GET podemos buscar uma 
chave inexistente, caso não haja um condição o Python irá simplesmente ignorar porém
se estabelecermos para condição de retorno o Python apresentará a mesma quando a chave
não existir, neste caso uma lista vazia 
"""

person_one = {
    'name': 'Larissa Almeida Conceição',
    'age': 23,
    'courses': [
        'Python',
        'React'
    ]
}

print(person_one)

person_one['name'] = 'Larissa de Almeida Conceição'
person_one['age'] = 24
person_one['courses'].append('Django')

print(person_one)

"""
No exemplo acima podemos ver que uma vez que acessamos a chave do dicionário podemos
alterar a informação ou então adicionar um novo valor como fizemos na lista através
do append()
"""

person_one.pop('age')
print(person_one)

"""
O pop() neste caso irá ler o valor e em seguida o removerá do dicionário
"""

person_one.update({'age': 24, 'gender': 'F'})
print(person_one)

"""
Já no exemplo acima estamos adicionando novos valores ao dicionário através do método update()
o qual atualiza o mesmo
"""

person_one.clear()
print(person_one)

"""
O clear() limpará todas as informações entregando assim um dicionário vazio
"""
