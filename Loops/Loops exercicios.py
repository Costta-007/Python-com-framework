# 1


# c =  0
# while c <= 5:
#     print(c)
#     c =  c + 1

# n =  int(input('numero: '))


# for x in range(1,11):
#     c = x * n
#     print(n , 'x', x , '=', c ) 

# ============================================================================================================================

### **2. Contagem Regressiva com Pausa**

# Peça um número inteiro positivo. Use `while` para fazer uma contagem regressiva até 0, exibindo cada número. Após o término, exiba `"Fogo!"`.

# i = int(input("Digite um inteiro positivo: "))

# while i >=0:
#     print(i)
#     i-=1
# print("Fogo!")

### **3. Média de Notas com `while`**

# Peça notas até que o usuário digite `-1`. Calcule e exiba a média das notas válidas (0 a 10). Ignore entradas inválidas e use `continue` quando necessário.
# d = "s"
# notas = []
# while d =="s":
#     try:
#         n = float(input("Digite uma nota: "))
#         notas.append(n)
#     except ValueError:
#         print("Ops, não foi um numero...")
#     d = input("Continuar?(s/n)")
# print("A media será",sum(notas)/ len(notas))

#===============================================================================

### **4. Validação de Senha com Limite de Tentativas**

# Defina uma senha fixa (ex: `"python123"`). Dê ao usuário 3 tentativas usando `while`. 
# Se acertar, exiba `"Acesso liberado"` e encerre. Se errar todas, exiba `"Conta bloqueada"`.

dados = {
    "usuario":"Gustavo",
    "senha":"1234"
}

print("login")

i = 1
while i <4:
    u = input("Usuario: ")
    s = input("senha")
    if u == dados["usuario"] and s == dados["senha"]:
        print("Login efetuado")
        break
    else:
        print("Dados incorretos")
        i+=1
        
else:
    print("Conta bloqueada")