# Crie um programa que:


# Peça ao usuário dois números.


# Mostre:

# A soma, subtração, multiplicação e divisão.

# Verifique:

# Se os números são iguais.

# Se o primeiro número é maior que o segundo.

# Se pelo menos um dos números é maior que 10.

x = float(input("Digite o primeiro numero:"))
y = float(input("Digite o segundo numero:"))
#r = int(x>10) + int(y>10)
#Não podia usar "or"
print("============================")
print(f"A soma será: {x+y}\nA subtração será: {x-y}\nA divisão será: {x/y}\nE a multiplicação será: {x*y}")
print("============================")
print(f"Os numeros são iguais?------- {x==y}")
print(f"O primeiro é maior que o segundo?------- {x>y}")
print(f"Algum dos numeros é maior que 10?--------- {bool(int(x>10) + int(y>10))}")
print("============================")
#                                                            #Não pode usar "or"