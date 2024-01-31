# Com variável fixa e sem formatação

salary = 3800.00
outgoing = 2700.00

result = outgoing / salary * 100

print(result)

# Com variável dinâmica e formatação

salary = float(input("Digite o seu salário líquido: "))
outgoing = float(input("Digite o valor das suas despesas: "))

result = outgoing / salary * 100

print(f"{result:.2f}")
