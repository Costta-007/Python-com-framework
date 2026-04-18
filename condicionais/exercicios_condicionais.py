# # ### **. Classificação de Notas com Menção**

# # Crie um programa que leia a nota de um aluno (0 a 10) e exiba a menção correspondente:

# # - `"Excelente"` se nota >= 9
# # - `"Bom"` se nota >= 7 e < 9
# # - `"Regular"` se nota >= 5 e < 7
# # - `"Insuficiente"` se nota < 5

# nota = float(input("Nota do aluno: "))
# if nota >= 9:
#     print("excelente")
# elif nota >= 7 and nota <9:
#     print("Bom")
# elif nota >=5 and nota <7:
#     print("Regular")
# else:
#     print("Insuficiente")

#===================================================================

### **2. Validação de Triângulo**

# Leia três lados de um triângulo. Verifique se eles formam um triângulo (cada lado é menor que a soma dos outros dois). Se sim, classifique como:

# - `"Equilátero"` (todos os lados iguais)
# - `"Isósceles"` (dois lados iguais)
# - `"Escaleno"` (todos diferentes)

# l1 = float(input("Lado 1: "))
# l2 = float(input("Lado 2: "))
# l3 = float(input("Lado 3: "))

# if (l1 > l2+l3 or l2 > l1+l3 or l3>l1+l2):
#     print("Não é um triângulo")
# elif l1 == l2 == l3:
#     print("Triãngulo equilatero")
# elif l1==l2 or l2==l3 or l1==l3:
#     print("Isosceles")
# else:
#     print("Escaleno")

    #===================================================================

# ### **3. Cálculo de IMC com Faixas**

# Leia peso (kg) e altura (m). Calcule o IMC e classifique conforme a tabela da OMS:

# - `"Abaixo do peso"` se IMC < 18.5
# - `"Peso normal"` se 18.5 ≤ IMC < 25 
# - `"Sobrepeso"` se 25 ≤ IMC < 30 
# - `"Obesidade"` se IMC ≥ 30

# peso = float(input("Peso em kg: "))
# Altura = float(input("Altura em metros: "))
# imc = peso / (Altura**2)
# print(imc)
# if imc <18.5:
#     print("Abaixo do peso")
# elif imc >= 18.5 and imc < 25:
#     print("Peso normal")
# elif imc>=25 and imc <30:
#     print("Sobrepeso")
# else: 
#     print("Obesidade")

#===================================================================

### **4. Imposto de Renda Simplificado**

# Leia o salário bruto mensal e calcule o desconto do INSS (11% sobre o salário, limitado a R$ 1.500,00) e o IRRF conforme tabela:

# - Isento se salário bruto ≤ R$ 2.500,00
# - 7,5% sobre o que exceder R$ 2.500,00 até R$ 3.500,00
# - 15% sobre o que exceder R$ 3.500,00 até R$ 5.000,00
# - 27,5% sobre o que exceder R$ 5.000,00
    
#     Exiba o salário líquido após os descontos.

# b = float(input("Salario bruto: "))
# inss = b * 0.11
# if inss >1500:
#     inss = 1500
# irrf = 0

# if b <= 2500:
#     irrf = 0
# elif b >2500 and b <=3500:
#     irrf = b * 0.075
# elif b>3500 and b <=5000:
#     irrf = b * 0.15
# else:
#     irrf = b * 0.275

# l = b - irrf - inss
# print(f"Salario liquido: {l}")

#===================================================================

# ### **5. Jogo de Pedra, Papel e Tesoura**

# Leia duas jogadas (`"pedra"`, `"papel"` ou `"tesoura"`) e determine o vencedor ou empate. Use condicionais aninhadas.

 
# print("(1) pedra / (2) papel / (3) tesoura")
# j1 = int(input("Jogador 1: "))
# j2 = int(input("Jogador 2: "))

# if j1==j2:
#     print("Empate!")
# elif j1 == 1 and j2 == 3 or j1 == 3 and j2 == 2 or j1 == 2 and j2 == 1:
#     print("Jogador 1 venceu!")
# else:
#     print("Jogador 2 venceu!")

#===================================================================

### **6. Aprovação com Recuperação**

# Leia a nota da N1 e N2. Calcule a média (`(N1+N2)/2`). Se média ≥ 7, aprovado. Se média < 4, reprovado. 
# Caso contrário, o aluno vai para recuperação. Nesse caso, leia a nota da recuperação (NR). A média final é `(média + NR)/2`. Se média final ≥ 5, aprovado; senão, reprovado.

# n1 = float(input("Nota 1: "))
# n2 = float(input("Nota 2: "))
# media = (n1+n2) / 2

# if media >=7:
#     print("Aprovado")
# elif media < 4:
#     print("Reprovado")
# else:
#     print("Foi para recuperação...")
#     Nr= float(input("Nota da recuperação: "))
#     mediaf = (media + Nr)/2
#     if mediaf >= 5:
#         print("Aprovado por recuperação")
#     else:
#         print("Reprovado, mesmo em recuperação")

#===================================================================

### **7. Alistamento Militar**

# Se sexo for F, exiba "Não obrigatório".

# Se sexo for M, calcule a idade. Se idade < 18, exiba o tempo restante. Se idade = 18, exiba "Aliste-se imediatamente". 
# Se idade > 18 e ≤ 45, exiba "Já passou do prazo". Se idade > 45, exiba "Dispensado por idade".

# Se houver deficiência, altere a mensagem para "Dispensado por condição de saúde" (prioridade sobre outras mensagens).
# sexo =input("Qual seu sexo?(M/F): ")
# ano = int(input("Que ano você nasceu?: "))
# deficiencia = input("Possui deficiencia?(s/n): ")
# idade = 2026 - ano

# if sexo == "m" or sexo =="M":
#     if idade <18:
#         print(f"Você ainda tem {18 - ano} até se alistar")
#     elif idade == 18:
#         print("Aliste-se imediatamente!")
#     elif idade >18 and idade <= 45:
#         print("Já passou do prazo")
#     else: 
#         print("Dispensado por idade")
# else:
#     print("Alistamento não obrigatorio")




#===================================================================


### **8. Escolha de Plano de Saúde**

# Leia a idade do cliente e o tipo de plano (`"basico"`, `"standard"`, `"premium"`). O valor mensal é calculado como:

# - Básico: R$ 100 + (idade * 2)
# - Standard: R$ 150 + (idade * 3)
# - Premium: R$ 200 + (idade * 5)
    
#     Se o cliente tiver mais de 60 anos, há um acréscimo de 10% sobre o valor total.
# preco = 1
# i = int(input("Idade: "))
# if i >60:
#     preco = 1.1
# p = int(input("""
# Planos:
# (1)Basico
# (2)Standard
# (3)Premium

# Qual o seu plano?\n
# """))

# if p == 1:
#     print(f"O preço será R${(100 + i * 2) * preco:,.2f}")
# elif p ==2:
#     print(f"o preço será R${(150 + i * 3) * preco:,.2f}")
# elif p == 3:
#     print(f"O preço será R${(200 + i * 5) * preco:,.2f}")

### **9. Validação de Data**

# Leia um dia (1-31), mês (1-12) e ano (qualquer). Verifique se a data é válida, considerando meses com 30/31 
# dias e fevereiro (28 ou 29 dias, considerando ano bissexto: divisível por 400 ou (divisível por 4 e não por 100)).
# dias = [31,28,31,30,31,30,31,31,30,31,30,31]

# d = int(input("Dia: "))
# m = int(input("Mês: "))
# ano = int(input("Ano: "))
# bissexto = ano % 4 == 0 and ano % 100 !=0



# if bissexto:
#     dias[1] = 29

# if m >= len(dias) or m <= 0:
#     print("Mês inexistente")
# elif d > dias[m-1] or d <= 0:
#     print("Dia inexistente") 
# else:
#     print(f"A data {d}/{m}/{ano} é real")

### **10. Simulador de Caixa Eletrônico**

# Leia o valor a ser sacado (inteiro, múltiplo de 5, entre 10 e 1000). Calcule a menor quantidade possível de notas de 50, 20, 10 e 5. 
# Exiba a quantidade de cada nota. Caso o valor não esteja dentro das regras, exiba uma mensagem de erro.

sac = int(input("Valor a ser sacado: "))
#785
if not sac % 5 == 0 or sac <10 and sac > 1000:
    print("Preciso de um multiplo de 5 que esteja entre 10 e 1000")
else:
    notas50 = sac//50
    sac = sac - 50*(notas50)
    notas20 = sac//20
    sac = sac-20*(notas20)
    notas10 = sac//10
    sac = sac - 10*(notas10)
    notas5 = sac//5
    sac = sac - 5*(notas5)
    print(f"Notas de 50 : {notas50} \nNotas de 20: {notas20}\nNotas de 10: {notas10} \nNotas de 5: {notas5}")