# 1. Verificação de maioridade e permissão
# Enunciado:
# Crie um programa que leia a idade do usuário e se ele possui autorização dos pais 
# (responda True ou False).
# O usuário pode participar da atividade se tiver 18 anos ou mais ou 
# tiver autorização dos pais.
# Use and / or para verificar e exiba "Pode participar" ou "Não pode participar".


# idade = int(input('Idade: '))
# autorizacao = input('True ou False: ')
# participar = (autorizacao == bool('True') and idade >= 18) and 'Pode participar' or 'Não pode participar'


# print(participar)

# =========================================================================================================

# 2. Classificação de peso ideal
# Enunciado:
# Leia o peso (kg) e a altura (m) de uma pessoa. Calcule o IMC (peso / altura**2).
# Uma pessoa está com peso normal se o IMC estiver entre 18.5 e 24.9 (inclusive).
# Use operadores lógicos para verificar se o IMC está nessa faixa e exiba 
# "Peso normal" ou "Fora da faixa".

# peso = float(input("Peso(kg): "))
# altura = float(input("Altura(m): "))
# imc = (peso/(altura**2))
# print(imc)
# verificar2 = imc>=18.5 and imc<=24.9 and "Peso normal" or "Fora da faixa"
# print(verificar2)

# =========================================================================================================

# 3. Acesso ao sistema
# Enunciado:
# Leia o nome de usuário e a senha. O acesso é permitido apenas se o usuário 
# "admin" e a senha for "1234".
# Use and para verificar as duas condições e exiba "Acesso liberado" 
# ou "Acesso negado".

# user=input("Usuario:")
# senha=input("Senha:")

# verificar3 = user=="admin" and senha=="1234" and "acesso liberado" or "acesso negado"
# print(verificar3)

# =========================================================================================================

# 4. Compra com desconto
# Enunciado:
# Leia o valor da compra e se o cliente é VIP (True ou False).
# O cliente ganha 10% de desconto se o valor for maior que R$ 100 ou ele for VIP.
# Exiba o valor final com desconto (se aplicável) ou o valor original.


# vip=(input("Vip(True or False):"))
# valor= float(input("Valor gasto:"))
# print(vip)
# verificar = vip=="True" and f"Você recebeu descono e pagará R${valor * 0.9} pois é VIP" or valor > 100 and f"Voce recebeu descono e pagará R${ valor * 0.9} pois gastou mais de R$100" or f"Você pagará {valor} que é o valor cheio"
# print(verificar)

# =========================================================================================================

# 5. Elegibilidade para doação de sangue
# Enunciado:
# Leia a idade e o peso.
# Para doar sangue, a pessoa deve ter entre 16 e 69 anos (inclusive) e pesar pelo menos 50 kg.
# Use and para verificar ambos os critérios e informe se a pessoa pode doar.

# idade = int(input("Idade:"))
# peso = float(input("Peso(kg):"))

# verificar = idade>=16 and idade<=59 and peso >=50 and "Pode doar" or "Não pode doar"
# print(verificar)

# =========================================================================================================

# 6. Validação de horário de funcionamento
# Enunciado:
# Uma loja funciona de segunda a sexta, das 9h às 18h.
# Leia o dia da semana (1=segunda, 7=domingo) e a hora (0 a 23).
# Determine se a loja está aberta.
# Dica: use and para combinar dia útil com horário, e or se quiser tratar sábado/domingo como fechado.

# dia = int(input("Dia:"))
# hora = int(input("Hora:"))

# verificar = dia >=1 and dia <=5 and hora >=9 and hora <=18 and "Loja aberta "or "Loja fechada"
# print(verificar)

# =========================================================================================================

# 7. Aprovação em duas disciplinas
# Enunciado:
# Leia as notas de Matemática e Português.
# O aluno é aprovado se ambas as notas forem maiores ou iguais a 6.
# Use and para verificar e exiba "Aprovado" ou "Reprovado".

# nota_mat = float(input("Nota matematica:"))
# nota_pt = float (input("Nota portugues:"))

# verificar = nota_mat>=6 and nota_pt >= 6 and "aprovado" or "reprovado"
# print(verificar)

# =========================================================================================================

# 8. Identificação de ano bissexto
# Enunciado:
# Um ano é bissexto se for divisível por 4, mas não por 100, a menos que também seja divisível por 400.
# Leia um ano e use and e or para determinar se ele é bissexto.
# Exiba "Ano bissexto" ou "Ano não bissexto".

# print(" é bissexto????")
# ano = int(input("Ano:"))

# verificar = (ano % 4) == 0 and (ano % 100) != 0 and (ano % 400) != 0 and "Ano bissexto" or "Não bissexto"
# print(verificar)

# =========================================================================================================

# 9. Faixa etária
# Enunciado:
# Leia a idade e classifique:

# "Criança" se idade < 12

# "Adolescente" se 12 ≤ idade ≤ 17

# "Adulto" se idade ≥ 18
# Use and e or para definir os intervalos e exiba a classificação.

# idade = int(input("idade:"))

# verificar9 = idade < 12 and "Criança" or idade <=17 and "adolescente" or idade >=18 and "Adulto"
# print(verificar9)

# =========================================================================================================

# 10. Sistema de alerta de temperatura e umidade
# Enunciado:
# Leia a temperatura (°C) e a umidade (%).
# Dispare um alerta se temperatura > 35 ou umidade > 70.
# Caso contrário, exiba "Condições normais".
# Use or para combinar as condições.

# temp=float(input("Temperatura(C°):"))
# umidade = int(input("Umidade(%):"))
# verificar10= temp >35 and umidade > 70 and "Alerta" or "Normalidade"
# print(verificar10)

# =========================================================================================================

# Desafio:

# Contexto:

# Uma indústria monitora temperatura (T), umidade (U) e presença de gás inflamável (G, 0 ou 1).

# O nível de risco é dado por:

# Crítico: (T > 40 ou U > 80) e G == 1

# Alto: (T > 40 ou U > 80) e G == 0

# Médio: (T entre 25 e 40) e (U entre 50 e 80)

# Baixo: qualquer outra situação

# t = float(input("temperatura:"))
# u = int(input("Umidade:"))
# g = input("Gás(True ou False):")

# verificar_desafio = (t>40 or u>80) and g== "True" and "CRITICO" or (t>40 or u>80) and g== "False" and "ALTO" or t>=25 and t<=40 and u>=50 and u<=80 and "MÉDIO" or "BAIXO"
# print(verificar_desafio)









# Use dicionário, variáveis ou listas … 

# Contexto:
# Uma loja oferece um cupom especial. O cliente ganha o cupom se atender a pelo menos  das seguintes condições:

# Se for VIP (responde "sim" ou "não")
# Valor da compra acima de R$ 200
# Primeira compra no mês (responder "sim" ou "nao")

# Além disso, o cupom  pode ser aplicado se o cliente tiver  no histórico. 

# Tarefa Receba:

# vip (string "sim" ou "nao")
# valor (float)
# primeira_compra (string "sim" ou "nao")
# Reclamação 

# Determine se o cliente  ("Cupom liberado") ou  ("Sem cupom"),  (SEM IF , SEM LOOP, SEM FUNÇÃO)




vip = input("Vip?(s/n):")
valor = float(input("Valor(R$):"))
primeira_compra=input("É a primeira compra do mês?(s/n):")
verificar11= (vip=="s" or valor >200 or primeira_compra=="s") and "Cupom liberado" or "Sem cupom"
print(verificar11)

