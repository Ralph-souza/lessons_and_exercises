# Tipo Texto (String)

"""
Como já mencionamos em etapas anteriores temos aqui um tipo de dado 
com formato textual, e em linguagem Python entendemos como texto tudo
aquilo que se encontra entre aspas ('').
Antes de mais nada se acessarmos o shell (terminal interativo) do Python
poderemos ver tudo que o método str() abrange.
"""

name = 'Ralph Souza'
print(name)
print(name[0])

"""
No segundo exemplo o que estamos fazendo é acessar através do índice um letra
que compõe a string, numa string todos os componentes são indexados e têm
início sempre pelo índice 0(zero)
"""

# new_letter = name[0] = 'S'
# print(new_letter)

"""
Se executarmos o exemplo acima teremos um erro indicando que a string não pode ser
alterada, isso por que strings são imutáveis, podemos mudar o conteúdo de uma variável
mas não o conteúdo da string em si
"""

item = "marca d'água"
print(item)

"""
O exemplo acima é importante para nos atentarmos na maneira como damos início a string
visto que a mesma pode se escrita com aspas simples(''), por assim dizer ou
aspas duplas("")
"""

new_name = 'Dias D\' Ávila'
print(new_name)

"""
Uma maneira de lidar com essa situação seria utilizando o scapping, nada mais do que a 
aplicação da barra inclinada que vemos após o D fazendo com que o Python entenda que
a aspas simples faz parte do texto
"""

text = 'Texto entre apostrófos pode ter "aspas"'
print(text)

doc = """Isto é um texto de
... múltiplas linhas"""
print(doc)

new_doc = "Aqui usamos a \n quebra de linha"
print(new_doc)

"""
Acima teremos alguns exemplos de como podemos trabalhar strings, quando usamos 3(três) aspas("")
criamos um texto de múltiplas linhas porém, se só quisermos que um texto seja 'quebrado'
em mais de uma linha usamos '\n', o qual executará essa função
"""

second_name = 'Larissa Almeida'
print(second_name[-2])

"""
A leitura da STRING é feita no formato ocidental, ou seja, da esquerda para a direita porém,
é possível ler os índices de trás para frente como podemos ver no exemplo acima através
do '[-]'
"""

print(second_name[4:])

"""
No exemplo acima estou atuando à partir de um range, ou seja, a partir do índice [4]
"""

print(second_name[-5:])

"""
Também posso fazer este processo no sentido inverso, começando como no exemplo acima, a partir do índice
[-5] até o final
"""

print(second_name[:4])

"""
Já no exemplo acima eu saio do começo e vou até determinado índice, lembrando que o índice [4] não aparecerá
"""

print(second_name[2:5])

"""
No exemplo acima estabeleço um range que começa no índice [2] e vai até o [5] sendo que ele trará o índice
de início mas não trará o índice de encerramento do range 
"""

print(second_name) # O resultado dessa operação será 'Larissa Almeida'
print(second_name[::]) # O resultado desta operação será o mesmo de cima

print(second_name[::2])

"""
Já neste último exemplo estabelecemos que ele pegará todos os índices, do primeiro [0] ao último [15] da nossa 
string porém, fará isso de dois em dois, assim sendo o terceiro valor aplicado seria o STEP que estabeleci para
a execução
"""

print(second_name[1::2])

"""
Neste exemplo acima estamos determinando de qual índice iremos partir e seguindo o mesmo step de 2 em 2
"""

print(second_name[::-1])

"""
Já neste exemplo estamos trazendo do começo até o fim só que começando pelo último índice, se eu colocar [::-2]
ele fará essa mesma inversão só que de dois em dois
"""

print(len(second_name))

"""
O len() nos dá o tamanho total da string
"""

print(second_name.lower())
print(second_name)

"""
O lower() converte todas as letras para minúsculo sem mudar a string
"""

print(second_name.upper())
print(second_name)

"""
O mesmo acontece com o upper() convertendo tudo para maiúscula sem mudar a string
"""

print(second_name.split())

"""
O split() irá separar as palavras contidas na string, como não demos um parâmatro para o split()
ele separará levando em consideração os espaços em branco
"""

print(second_name.split('i'))

"""
Ao passarmos um parâmentro o mesmo separará a string com base no parâmetro estabelecido
"""
