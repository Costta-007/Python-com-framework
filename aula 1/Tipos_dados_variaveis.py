# # dados 
# # scrip - interpretar -  resposta 
# # lógica + melhorar 
# # memória ram - curta duração

# # 4 tipos

# # cadastro 
# # nome idade email peso altura endereco
# # salario > 2000

# # texto   -  "text"  'text'  -  nome  - email - endereco
# # inteiro - 10,  0  ,  -1  -  idade 
# # decimal - 5.2, 9.10,0.  - peso  - altura  - 
# # lógico  - True ,  False  -  saslario
# #            1        0

# print(10 + 2)
# print(True + 10)
# print(5.2 + 5)
# print('text' + "fhsdjkfh")
# print('fhsdgfhsdgfs')


# # concatenação juntar dados

# # print('Olá', 'João')
# # print(f'Olá {'João'}')

# # # indentação -  organizar o código

# # print()


# # # variáveis

# # imc = 0

# # # Não podem por numero
# # # caracteres especiais # @% &*

# # # pode começar por letra
# # # _ underline pode utilizar

# # # seguida de um igual 

# # # ESTRUTURA DE DADO

# # imc = 0 
# # altura  =  1.70
# # peso = 62.0
# # imc =  peso // (altura ** 2)
# # print(imc)

# # # sinais aritméticos 
# # # +   -    *   /   %   **  // 

# # print('SINAIS ARITMÉTICOS')
# # # saida sem é um número 

# # x = 10
# # y = 20
# # x = 200

# # print(x + y)
# # print(x - y)
# # print(x / y)
# # print(x * y)
# # print(x ** y)


# # print(x // y)
# # print(x % y)


# # # sinais lógicos 
# # y = 20
# # x = 200
# # print(x == y) # comparação
# # print(x > y) # maior
# # print(x < y) # menor
# # print(x >= y) # maior ou igual
# # print(x <= y) # menor ou igual
# # print(x != y) # diferente

# # Crie um programa que:


# # Peça ao usuário dois números.


# # Mostre:

# # A soma, subtração, multiplicação e divisão.

# # Verifique:

# # Se os números são iguais.

# # Se o primeiro número é maior que o segundo.

# # Se pelo menos um dos números é maior que 10.

# # x = float(input("Digite o primeiro numero:"))
# # y = float(input("Digite o segundo numero:"))

# # print(f"""A soma será {x+y}\nA subtração será {x-y}\nA divisão será {x/y}\nE a multiplicação será {x*y}""")
# # if (x == y):
# #     print("Os numeros eram iguais!")
# # if x>y:
# #     print("O primeiro numero é maior que o segundo")
# # if x>10 or y>10:
# #     print("Um dos numeros é maior do que 10!")
    
# print() # imprime algo ambiente de teste 


# var =  10 # variáveis 


# # nome = input('Digite seu nome:  ') # dinamico 
# # # 


# # print(nome)


# # nome  = 'Julia'


# # nome  =  input('Nome: ')



# print('CADASTRE SEUS DADOS: ')
# # int()  float() str() bool() type casting


# nome = input('Nome: ')
# idade  = int(input('Idade: ')) + 10
# endereco  = input('Endereço: ')
# curso = input('Curso: ')
# altura = float(input('Altura'))
# saldo_banco = float(input('Saldo: '))


# print('NOME:', nome)
# print('IDADE:', idade)
# print('ENDEREÇO:', endereco)
# print('CURSO:', curso)
# print('ALTURA:', altura)
# print('SALDO NO BANCO:', saldo_banco)


lista = []
lista_2 = [1,2,3,4,5,6,7,8,9]
lista_3 = list(range(1,2000))

#função para adicionar

lista_2.append(110)
lista_2.insert(0,300)
lista_2.extend([10,10,10,10,10])
lista_2 += (20,2012312321,20,20)
print(lista_2)
#função para remover

lista_2.remove(2012312321)
print(lista_2)
lista_2.pop()
print(lista_2)
lista_2.pop(1)
print(lista_2)
del lista_2[2]
print(lista_2)
#slice - fatiamento
