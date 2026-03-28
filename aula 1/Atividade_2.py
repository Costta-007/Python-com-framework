# Peça o valor de um produto e: 

# Calcule um desconto de 10%.


# Mostre o valor final.


# Verifique se o valor final é maior que 100.


# Verifique se o produto ficou barato (menor que 50).
print("============================")
valor = float(input("Qual o valor do produto?:"))
valor_desconto = valor - (valor * 0.1)
print("============================")
print(f"O valor com desconto fica: {valor_desconto}")
print(f"O valor é acima de 100? : {valor_desconto>100}")
print(f"Esta barato?: {valor_desconto < 50}")
print("============================")