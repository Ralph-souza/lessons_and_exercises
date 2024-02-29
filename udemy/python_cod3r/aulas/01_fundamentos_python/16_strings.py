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
 