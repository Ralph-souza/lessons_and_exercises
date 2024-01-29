# Tipos básicos
# Vale lembrar que toda linguagem segue uma regra e a estrutura de dados serve como delimitador para essas regras
# e como os dados deverão se comportar.
# Alguns dos tipos são:

# Booleano -> Basicamente valida um status de verdadeiro ou falso de um dado
print(True)
print(False)

# Ponto flutuante (números reais) -> Qualquer valor seguido de ponto e fração do mesmo
print(2.5)

# Inteiros -> Sem quebras ou frações
print(2)

# Strings -> Texto em geral
print("Teste de texto")

# Concatenação
# Nada mais e do que a possibilidade de unir dados de diferentes tipos, usa o sinal de (+) mas não efetua soma
# apenas une os valores em uma sentença, por exemplo:

print("Você é " + 3 * "muito " + "legal!")
# No exemplo acima nós temos uma string (texto) inicial ("Você é ", seguida de uma string que será repetida
# 3(três) vezes ("muito ") mais uma string de conclusão da frase ("legal!") tendo como resultado final a sentença
# Voce e muito muito muito legal. Neste caso nao e possivel somar valores se um estiver tipado com string e
# outro inteiro, por exemplo: "3" + 3

# Podemos usar + para somar contudo desde que ambos valores sejam de tipo inteiro ou ponto flutuante. Por exemplo:

print(2.5 + 3)
# Neste exemplo teremos como resultado da soma o valor 5.5

# Tipo vazio ou inexistente
print(None)

# Temos outros tipos de estrutura de dados como:

# Lista -> Serve para armazenar um grupo de valores dentro de uma única estrutura, sendo dinâmica e organizada por
# indices que se iniciam em 0, ou seja, no exemplo acima tem a seguinte lista [1, 2, 3] as posições para cada item
# serão categoricamente [0][1][2], na lista acessamos os dados contidos através do índice do mesmo,
# outros pontos importantes são, uma lista é mutável podendo receber novos valores e sua estrutura base e definida
# pelo uso de colchetes []

print([1, 2, 3])

# Dicionario -> Estrutura que utiliza chave e valor tendo sua estrutura base definida pelo uso de chaves {}
# e acessamos os valores através das chaves de cada valor

print({"nome": "Fulano", "sobrenome": "da Silva", "idade": 30})
