# Operadores Membro/Identidade

"""
São operadores de validação como IS e IN
"""

commom_list = [1, 2, 3, 'Anna', 'Carol']
# Uma lista comum contendo alguns itens e iremos verificar se:

# Membro
print(2 in commom_list) # Resultado TRUE
"""
Visto que 2 está na lista o resultado será TRUE
"""

print('Anna' not in commom_list) # Resultado FALSE
"""
Visto que 'Anna' está na lista o resultado desta operação é FALSE
"""

# Identidade

x = 3
y = x
z = 3

print(x is y)
print(y is z)
print(x is not z)

"""
Os resultados dessas operações serão respectivamente:

True
True
False

Por isso? X e Z possuem o mesmo valor então compará-los significa comparar seus valore que 
são iguais, assim como Y que recebe X, portanto dizer que X não é igual a Z (por assim dizer)
dará FALSE visto que o que está sendo comparado é o valor contido na variável e não seu
identificador(nome) em si.
"""

list_a = [1, 2, 3]
list_b = list_a
list_c = [1, 2, 3]

print(list_a is list_b)
print(list_b is list_c)
print(list_a is not list_c)

"""
Os resultados provenientes desses processos em lista serão:

True
False
True

Porém, comparado ao teste de variáveis LIST_B e LIST_C são diferentes e isso está refletido no 
resultado FALSE na linha 56, por quê? Basicamente a quando criamos a LIST_A ela passa a ser armazenada
em um espaço específico de memória, quando criamos a LIST_B está por receber LISTA_A está apontando para
o mesmo espaço de memória por isso são iguais poreḿ, quando criamos LIST_C esta é aramazenada em 
um novo espaço criando assim uma nova identidade, sendo assim, mesmo que possuam os mesmos valores 
não serão iguais, visto que um espaço armazena uma determinada lista e ou espaço uma outra lista. 
Diferente de variáveis que guardam um valor.
"""
