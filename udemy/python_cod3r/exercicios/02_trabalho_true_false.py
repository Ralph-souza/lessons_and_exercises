# Desafio Operadores Lógicos

"""
Em resumo: Um pai de família possui a possibilidade de realizar 2 trabalhos, a realização de
ambos (terça e quinta) permite a família comprar uma TV 50" e tomar sorvete em comemoração. 
Já a realização de 1(um) trabalho permite a família a compra de uma TV 32" e tomar sorvete contudo,
não realizar nenhum faz com que a família permaneça em casa.
"""

# Os Trabalhos

# Estrutura base do desafio
tuesday = True
thursday = False

tv_50 = tuesday and thursday
tv_32 = tuesday != thursday # XOR ou Validação Exclusiva (ou um ou outro explicíto)
ice_cream = tuesday or thursday
stay_home = not ice_cream

"""
Confirmando os 2 trabalhos: TV 50" + Sorvete
Confirmando 1 trabalho: TV 32" + Sorvete
Nenhum trabalho: Fica em casa
"""

print("TV_50={} TV_32={} Ice_cream={} Stay_home={}".format(tv_50, tv_32, ice_cream, stay_home))
"""
A função .format() irá substituir cada uma das aréas entre chaves por um valor
damos a este tipo de processo o nome de interpolação, ou seja, a inserção de 
um trecho de texto dentro de outro
"""
