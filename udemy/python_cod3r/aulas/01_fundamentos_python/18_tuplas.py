# Tuplas

"""
Tuplas são estruturas imutáveis e são representadas pelo uso de 
parênteses '()'
"""

exe_tuple = ('um')
print(type(exe_tuple))

"""
Se usarmos dessa forma veremos que a resposta para o tipo será string,
por que isso? Porque os parênteses também são usados para criar uma expressão
"""

exe_tuple = ('um',)
print(type(exe_tuple))

"""
Para que possamos criar corretamente a tupla após o elemento aplicamos uma
vírgula(','), e agora sim como podemos ver na resposta temos uma tupla, isso 
para casos onde a tupla possui um único elemento
"""

print(exe_tuple[0])

"""
Tuplas são indexissáveis, assim sendo podemos acessar seus elementos através do
índice correspondente
"""
