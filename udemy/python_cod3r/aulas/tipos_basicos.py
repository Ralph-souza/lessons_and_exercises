# Tipos basicos
# Vale lembrar que toda linguagem segue uma regra e a estrutura de dados serve como delimitador para essas regras
# e como os dados deverao se comportar.
# Alguns dos tipos sao:

# Booleano -> Basicamente valida um status de verdadeiro ou falso de um dado
print(True)
print(False)

# Ponto flutuante (numeros reais) -> Qualquer valor seguido de ponto e fracao do mesmo
print(2.5)

# Inteiros -> Sem quebras ou fracoes
print(2)

# Strings -> Texto em geral
print("Teste de texto")

# Concatenacao
# Nada mais e do que a possibilidade de unir dados de diferentes tipos, usa o sinal de (+) mas n~ao efetua soma
# apenas une os valores em uma sentenca, por exemplo:

print("Voce e " + 3 * "muito " + "legal!")
# No exemplo acima nos teremos um string (texto) inicial ("Voce e ", seguida de uma string que sera repetida
# 3(tres) vezes ("muito ") mais uma string de conclusao da frase ("legal!") tendo como resultado final a sentenca
# Voce e muito muito muito legal. Neste caso nao e possivel somar valores se um estiver tipado com string e
# outro inteiro, por exemplo: "3" + 3

# Podemos usar + para somar contudo desde que ambos valores sejam de tipo inteiro ou ponto flutuante. Por exemplo:

print(2.5 + 3)
# Neste exemplo teremos como resultado da soma o valor 5.5

# Tipo vazio ou inexistente
print(None)

# Temos outros tipos de estrutura de dados como:

# Lista -> Serve para armazenar um grupo de valores dentro de uma unica estrutura, sendo dinamica e organizada por
# indices que se iniciam em 0, ou seja, no exemplo acima tem a seguinte lista [1, 2, 3] as posicoes para cada item
# serao categoricamente [0][1][2], na lista acessamos os dados contidos atraves do indice do mesmo,
# outros pontos importantes sao, uma lista e mutavel podendo receber novos valores e sua estrutura base e definida
# pelo uso de colchetes []

print([1, 2, 3])

# Dicionario -> Estrutura que utiliza chave e valor tendo sua estrutura base definida pelo uso de chaves {}
# e acessamos os valores atraves das chaves de cada valor

print({"nome": "Fulano", "sobrenome": "da Silva", "idade": 30})
