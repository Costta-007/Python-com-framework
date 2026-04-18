# # try:
# #     n1  = int(input('>>>'))
# #     n2  =  int(input('>>'))
# #     soma  =  n1 + n2
# #     lista  =  [n1, n2]
# #     i =  int(input('Indice: '))
# #     print(lista[i])
# #     numero =  int(input('numero:  '))
# #     print(float(numero))
# #     print(n1/n2)
    
# # except TypeError as erro:
# #     # tentando fazer o calculo aritmético
# #     # entre um numero e uma letra...
# #     print(erro)
# # except ValueError as erro:
# #     # quando tento imprimir uma letra em um input de numero
# #     print(erro)
# # except IndexError as erro:
# #     # indice que não existe na lista
# #     print(erro)
# # except ZeroDivisionError as erro:
# #     print(erro)
# # else:
# #     print('Erro não identificado')
# # finally:
# #     print('fim carregamento...')

# # idade =  int(input('Idade: '))
# # carta_m =  input('POssui carta sim ou não?')
# # decisao =  idade>=18 and carta_m == 'sim' and 'Pode dirigir' or 'não pode...'
# # print(decisao)

# # if idade >= 18 and carta_m == 'sim':
# #     print('Pode ')
# # else:
# #     print('Não pode')
    
# # if idade >= 18:
# #    if carta_m == 'sim':
# #        print('Pode ')
# # else:
# #     print('Não pode')
    
    
# # if idade >= 18 and carta_m == 'sim':
# #    print('Pode ')
# # elif idade >= 18 and carta_m == 'não':
# #    print('pode tirar a carta')
# # else:
# #    print('Não pode')

# # print("SISTEMA DE NOTAS")

# # alunos = []
# # a1 = input("Nome do aluno 1: ")
# # a2 = input("Nome do aluno 2: ")
# # alunos.append(a1)
# # alunos.append(a2)
# # print("Lista de alunos:", alunos)

# # notas_a1 = [float(input("nota_a: ")), float(input("nota_a: "))]
# # notas_a2 = [float(input("nota_B: ")), float(input("nota_B: "))]            
            
# # media_a1 = sum(notas_a1)/len(notas_a1)
# # media_a2 = sum(notas_a2)/len(notas_a2)
# # print(f"Media {a1}:{media_a1} e Media {a2}:{media_a2}")

# # if media_a1 >6:
# #     print(f"{a1} aprovado")
# # elif media_a1 >= 5 and media_a1<=6:
# #     print(f"{a1} recuperação")
# # else:
# #     print(f"{a1} reprovado")


# # if media_a2 >6:
# #     print(f"{a1} aprovado")
# # elif media_a2 >= 5 and media_a2 <=6:
# #     print(f"{a1} recuperação")
# # else:
# #     print(f"{a1} reprovado")

# # sistema de notas
# print('SISTEMA DE NOTAS')
# lista_nomes = []
# aluno_1 =  input('Digite o nome do aluno: ')
# aluno_2 =  input('Digite o nome do aluno: ')
# lista_nomes.append(aluno_1)
# lista_nomes.append(aluno_2)
# print('lista de alunos: ', lista_nomes)

# notas_aluno_1 = [float(input(f'nota1 {aluno_1}: ')), float(input(f'nota2 {aluno_1}: '))]
# notas_aluno_2 = [float(input(f'nota1 {aluno_2}: ')), float(input(f'nota2 {aluno_1}: '))]

# media_aluno_1 = sum(notas_aluno_1)/len(notas_aluno_1)
# media_aluno_2  = sum(notas_aluno_2)/len(notas_aluno_2)
# print('Aluno', aluno_1, 'Média', media_aluno_1)
# print('Aluno', aluno_2, 'Média', media_aluno_2)

# if media_aluno_1 > 6:
#     print('Aluno aprovado', aluno_1)
# elif media_aluno_1 >= 5 and media_aluno_1 <= 6:
#     print('Aluno de recuperação', aluno_1)
# else:
#     print('Aluno reprovado', aluno_1)

# print('.......................................')

# if media_aluno_2 > 6:
#     print('Aluno aprovado', aluno_2)
# elif media_aluno_2 >= 5 and media_aluno_2 <= 6:
#     print('Aluno de recuperação', aluno_2)
# else:
#     print('Aluno reprovado', aluno_2)


