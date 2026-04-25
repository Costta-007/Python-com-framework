### **1. Calculadora com Funções**

# Crie funções separadas para as quatro operações básicas (`somar`, `subtrair`, `multiplicar`, `dividir`). Em seguida, escreva um programa que leia dois números 
# e a operação desejada (como string) e chame a função correspondente. A divisão deve tratar divisão por zero.

# def somar(val1, val2):
#     return val1 + val2 
# def subt(val1,val2):
#     return val1 - val2
# def mult(val1, val2):
#     return val1 * val2
# def div(val1,val2):
#     return val1/val2

# def calc():
#     op = input("(1)-Soma\n(2)-Subtração\n(3)-Multiplicação\n(4)-Divisão\nQual a operação?: ")
#     x1 = int(input(""))
#     x2 = int(input(""))
#     if op == '1':
#         print(somar(x1,x2))
#     if op == '2':
#         print(subt(x1,x2))
#     if op == '3':
#         print(mult(x1,x2))
#     if op == '4':
#         try:
#             print(div(x1,x2)) 
#         except ZeroDivisionError:
#             print("Por 0 é impossivel")
# calc()



#===================================

### **2. Validador de CPF (simplificado)**

# Crie uma função `validar_cpf(cpf)` que recebe uma string com 11 dígitos e retorna `True` se for 
# válido (use o algoritmo básico de validação de CPF). Em seguida, teste a função com alguns CPFs.
# cpf = '52998224725'
# n = [int(x) for x in cpf]
# n1 = []
# c = 10

# def validar_cpf():
#     c = 10
#     for x in n:
#         if c >=2:
#             n1.append(x * c)
#             c -=1
#     oo = ((sum(n1) * 10 ) % 11) 

#     if oo == n[9]:
#         print("First number alright")
#         n1.clear()
#     else:
#         print(n1)
#         print("erro")

# #============
#     c = 11
#     for x in n:
#         if c >=2:
#             n1.append(x * c)
#             c -=1
    

#     oo = ((sum(n1) * 10 ) % 11) 

#     if oo == n[10]:
#         print(oo)
#         print("Second number alright")
#         print("Valid CPF")
#     else:
#         print("Invalid CPF")

# validar_cpf()


 
#++++++++++++++++++++++===================++++++++++++++++++++++++++++++++

#professora
# def verificar_cpf(cpf):
#     if len(cpf) != 11:
#         print('digite algo válido...')
#     else:
#         soma = 0
#         for x in range(9):
#             soma  = soma +  int(cpf[x]) * ( 10 - x) 
        
#         print((soma *10 ) % 11)
#         soma1 = 0
#         for x in range(10):
#             soma1  = soma1 +  int(cpf[x]) * ( 11 - x) 
#         print((soma1 *10 ) % 11)
        

# verificar_cpf('52998224725')            

