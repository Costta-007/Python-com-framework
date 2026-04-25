## **1. Tabuada Personalizada**

# Peça ao usuário um número inteiro positivo. Use `for` para exibir a tabuada desse número de 1 a 10.

# **Exemplo:**

# `Digite um número: 7` → exibe 7 x 1 = 7, 7 x 2 = 14, ..., 7 x 10 = 70.

# i = int(input("Digite um numero inteiro: "))

# for c in range(1,11):
#     print(f"{i} x {c} = {i * c}")

# ===========================================================================


### **2. Contagem Regressiva com Pausa**

# Peça um número inteiro positivo. Use `while` para fazer uma contagem regressiva até 0, exibindo cada número. Após o término, exiba `"Fogo!"`.

# c = int(input("Digite um numero inteiro positivo: "))

# while c >0:
#     print(c)
#     c-=1
# print("Fogo!")
# ===========================================================================

### **3. Média de Notas com `while`**

# Peça notas até que o usuário digite `-1`. Calcule e exiba a média das notas válidas (0 a 10). Ignore entradas inválidas e use `continue` quando necessário.

# notas = []
# i= ""
# while i != "-1":
#     i = input("Digite a nota: ")
#     if 0 <= float(i) <=10:
#         notas.append(float(i))
#     elif i == "-1":
#         break
#     else:
#         continue
    
# print(f"As média é: {sum(notas)/len(notas):.2f}")

# ===========================================================================

### **4. Validação de Senha com Limite de Tentativas**

# Defina uma senha fixa (ex: `"python123"`). Dê ao usuário 3 tentativas usando `while`. Se acertar, exiba `"Acesso liberado"` e encerre. Se errar todas, exiba `"Conta bloqueada"`.

# senha = "Euamobolodechocolate1234"
# t = 3
# while t >0:
#     a = input("Digite a senha: ")
#     if a == senha:
#         print("Acesso liberado")
#         break
#     else:
#         print("Tente novamente")
#         t -= 1

# ==========================================================================

### **5. Números Primos**

# Peça um número inteiro positivo e determine se ele é primo. Use `for` com `range` e `break` para otimizar.

# i = int(input("Digite um numero inteiro positivo: "))
# n = list(range(2,int(i**0.5) +1))


# for a in n:
#     if i % a == 0:
#         print("Numero nao primo")
#         break
#     else:
#         print("Numero primo")
#         break

# ==========================================================================

### **6. Sequência de Fibonacci**

# Gere os primeiros N termos da sequência de Fibonacci, onde N é informado pelo usuário. Use `for` ou `while` para iterar.
# n= int(input("Digite até qual posição na sequencia você quer saber fibonacci: "))

# n1 = int(input("Digite o termo inicial \"a\": "))
# n2 = int(input("Digite o termo inicial \"b\": "))


# p = 0
# e = 1
# # print(f"{n1}\n{n2}")
# for i in range(n):
#     p = n1 + n2
#     print(f"{p}")
#     if e == 1:
#         n1 = p
#     else:
#         n2 = p
#     e = e * -1

# ==========================================================================
### **7. Soma de Dígitos**

# Peça um número inteiro positivo e calcule a soma de seus dígitos. Use `while` para extrair os dígitos um a um.

# i = int(input("Digite um numero inteiro positivo: "))
# print(sum(range(i+1)))
    
# i = input("Digite um numero inteiro positivo: ")
# count = 0
# while count <=0:
    
#     z = [int(x) for x in i]
#     s = sum(z)

#     count += 1
# print(s)
     

# for a in str(i):
#     nums.append(int(a))
#     print(nums)
#     # int(nums[range(a)])
# print(f"A soma dos algarismos é: {sum(nums)}")

# ==========================================================================
# GEMINI
# Solicita o número ao usuário

# numero = int(input("Digite um número inteiro positivo: "))

# soma = 0

# # O loop continua enquanto ainda houver dígitos no número
# while numero > 0:
#     # Extrai o último dígito (resto da divisão por 10)
#     digito = numero % 10 
    
#     # Adiciona o dígito à soma total
#     soma += digito 
    
#     # Remove o último dígito do número (divisão inteira)
#     numero = numero // 10 

# print(f"A soma dos dígitos é: {soma}")

# ==========================================================================

### **8 Menu Interativo**

# Crie um menu que permaneça ativo até que o usuário escolha a opção `"Sair"`. As opções podem ser:

# - `1` – Exibir mensagem "Olá!"
# - `2` – Exibir a data/hora atual (use `import datetime`)
# - `3` – Sair

# Use `while True` e `break` para sair.
# from datetime import datetime
# hoje = datetime.now()
# hreal = hoje.strftime("%d/%m/%y %H:%M:%S")

# e = 0
# while True:
#     print('''      Menu
# (1) - Exibir \"Olá\"
# (2) - Exibir a data/hora atual
# (3) - sair''')
#     e = input("Digite a escolha: ")
#     if e == "1":
#         print("===========\nOlá!\n===========")
#     elif e == '2':
#         print(f"============\nData: {hreal}\n============")
#     elif e == "3":
#         print("Até logo!")
#         break

#===================================================

# Simule 100 lançamentos de um dado de 6 faces. Conte quantas vezes cada face foi sorteada e exiba o resultado. Use for e random.randint(1,6). (Importe random.)
# import random as rand


# dados = []
# for x in range(100):
#     i = rand.randint(1,6)
#     dados.append(i)

# contagem = [
#     dados.count(1), dados.count(2), dados.count(3),
#     dados.count(4) ,dados.count(5) ,dados.count(6)]
    

# for x in range(6):
#     print(f"Contagem de faces {x+1}: {contagem[x]}")
# print(sum(contagem))

                                                              
