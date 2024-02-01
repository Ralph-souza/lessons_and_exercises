# Operadores Ternários

"""
São operadores ternários àqueles que usam 3(três) operandos para executar uma função
"""

raining = True

print("My clothes are " + ("dry.", "wet.")[raining])
"""
Ao utilizarmos um operador ternário como no exemplo acima temos os 3(três) operandos 
sendo dois os valores 'DRY' e 'WET' contidos entre parênteses e o terceiro sendo a expressão RAINING
neste caso o que o Python avalia é a posição nas quais os valores foram aplicados, ou seja,
a primeira posição é FALSE e a segunda posição é TRUE.
"""

# Com uso das condicionais IF e ELSE

print("My clothes are " + ('wet.' if raining else 'dry.')) # O IF e ELSE valida a veracidade e aplica o caso de acordo
"""
Ainda não vimos a utilização do IF e ELSE porém aqui eles fazem exatemante o que as expressões significam,
ou seja, SE estiver chovendo(raining) aplique 'WET' caso contrário aplique 'DRY'.
E sim, este ainda é um exemplo ternário contendo dois valores (WET e DRY) e uma expressão ('RAINING')
"""
