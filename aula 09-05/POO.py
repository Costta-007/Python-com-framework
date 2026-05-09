

# class Pessoa:
#     def __init__(self, idade):
#         self.idade = idade    


#     def verificar_idade(self):
#         if self.idade <= 14:
#             print('Criança')
#         elif self.idade >=15 and self.idade <= 17:
#             print('adolescente')
#         elif self.idade >= 18 and self.idade <= 34:
#             print('jovem')
#         elif self.idade >= 35 and self.idade <=60:
#             print('Adulto')
#         else:
#             print('idoso')        


# pessoa =  Pessoa(17)
# pessoa.verificar_idade()
# ########################################
# # Crie uma ##classe Pessoa com os atributos nome e idade. Adicione um método apresentar() que exiba "Olá, meu nome é [nome] e tenho [idade] anos." Crie duas pessoas diferentes e chame o método.


# # criei a classe
# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade  = idade
# # criei o método
#     def apresentar(self):
#         print(f'Olá, meu nome é {self.nome}, eu tenho {self.idade}')
# # instaciei a classe
# pessoa1 =  Pessoa('Kaio',20)
# pessoa2 =  Pessoa('Maria',22)
# # usei o método na instancia 
# pessoa1.apresentar()
# pessoa2.apresentar()

# #####################################

# class Pessoa:
#     def __init__(self, idade):
#         self.idade = idade    


#     def verificar_idade(self):
#         if self.idade <= 14:
#             print('Criança')
#         elif self.idade >=15 and self.idade <= 17:
#             print('adolescente')
#         elif self.idade >= 18 and self.idade <= 34:
#             print('jovem')
#         elif self.idade >= 35 and self.idade <=60:
#             print('Adulto')
#         else:
#             print('idoso')        


# pessoa =  Pessoa(17)
# pessoa.verificar_idade()


#
#exercicios
#

### **.Classe Retângulo**

# Crie uma classe `Retangulo` com os atributos `largura` e `altura`. Adicione métodos:

# - `calcular_area()` – retorna a área
# - `calcular_perimetro()` – retorna o perímetro
    
#     Crie um retângulo com largura 5 e altura 3 e exiba sua área e perímetro.

# class Retangulo:
#     def __init__(self, largura, altura):
#         self.largura = largura
#         self.altura = altura

#     def calcular_area(self):
#         area = self.largura * self.altura
#         return area
    
#     def calcular_perimetro(self):
#         perimetro = (2*self.largura) + (2*self.altura)
#         return perimetro
    
# forma1 = Retangulo(15, 2)
# forma2= Retangulo(10,5)

# print(forma2.calcular_area())
# print(forma2.calcular_perimetro())
# print()
# print(forma1.calcular_area())
# print(forma1.calcular_perimetro())

### **Classe Conta Bancária**

# Crie uma classe `ContaBancaria` com:

# - Atributos: `titular`, `saldo` (inicial 0)
# - Métodos:
#     - `depositar(valor)`: acrescenta ao saldo
#     - `sacar(valor)`: se houver saldo suficiente, subtrai; senão, exibe `"Saldo insuficiente"`
#     - `exibir_saldo()`: mostra o saldo formatado
        
#         Crie uma conta, faça depósitos e saques e exiba o saldo.

# class Conta:
#     def __init__(self, titular,saldo):
#         self.titular = titular
#         self.saldo = saldo
    
#     def depositar(self,valor):
#         valor = int(input("Digite o valor do depósito: "))
#         self.saldo += valor
#         print("Depósito concluído")
    
#     def sacar(self,valor):
#         valor = int(input("Digite o valor do saque: "))
#         saldo -= valor
#         print("Saque concluído")

#     def exibir_saldo(self):
#         print(f"Seu saldo é {self.saldo}")

# conta1 = Conta("Gustavo", 0)
# conta2 = Conta("Cecilia", 100000000000000)

# conta1.depositar()
# conta1.exibir_saldo()



# def main():
#     print("Acesso de contas\n[1]\n[2]")
#     sel = 0
#     i = input()
#     if i == "1":
#         print(f"Titular: {conta1.titular}")
#         sel = 1
#     elif i =="2":
#         print(f"Titular: {conta1.titular}")
#         sel = 2
#     print("O que deseja?\n[1]Depósito\n[2]Saque\n[3]Verificação de saldo")
#     i2= int(input())
#     if sel == 1:
#         if i2 ==1:
#             conta1.depositar()
#         elif i2 == 2:
#             conta1.sacar()
#         elif i2 == 3:
#             conta1.exibir_saldo()
#     elif sel ==2:
#         if i2 ==1:
#             conta2.depositar()
#         elif i2 == 2:
#             conta2.sacar()
#         elif i2 == 3:
#             conta2.exibir_saldo()

# main()

###################################################################################################

### **Classe Produto**

# Crie uma classe `Produto` com:

# - Atributos: `nome`, `preco`, `quantidade_estoque`
# - Métodos:
#     - `total_estoque()`: retorna `preco * quantidade_estoque`
#     - `adicionar_estoque(quantidade)`: aumenta a quantidade
#     - `remover_estoque(quantidade)`: diminui, mas não permite ficar negativo
        
#         Crie um produto, altere o estoque e exiba o valor total.

# class Produto:
#     def __init__(self, nome,preco,estoque):
#         self.nome = nome
#         self.preco = preco
#         self.estoque = estoque
#     def total_estoque(self):
#         return self.estoque
#     def add_estoque(self):
#         qtd = int(input("Quantas irá adicionar?"))
#         self.estoque += qtd
#         print("Adicionado")
#     def rem_estoque(self):
#         if self.estoque > 0:
#             print(f"Há {self.estoque} unidades de {self.nome}")
#             qtd = int(input("Quantas remover?"))
#             self.estoque -= qtd
#         else:
#             print(f"Não há {mouse.nome} em estoque")

# mouse = Produto("mouse",10.99,0)

# mouse.rem_estoque()
# print(f"Há {mouse.estoque} {mouse.nome} no estoque\n")
#mouse.add_estoque()
#print(f"Há {mouse.total_estoque()} {mouse.nome} no estoque\n")

### **5. Classe Aluno**

# Crie uma classe `Aluno` com:

# - Atributos: `nome`, `matricula`, `notas` (lista de floats)
# - Métodos:
#     - `adicionar_nota(nota)`: adiciona à lista
#     - `calcular_media()`: retorna a média das notas
#     - `situacao()`: retorna `"Aprovado"` se média >= 7, `"Recuperação"` se >= 5, `"Reprovado"` caso contrário
        
#         Crie um aluno, adicione 3 notas e exiba sua situação.

class Aluno:
    def __init__(self, nome, matricula, notas):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas = []
     
    def add_nota(self, nota):
        self.notas.append(nota)
        print("Subiu")
        print(self.notas)

    def calc_media(self):
        media = (sum(self.notas)) / len(self.notas)
        return media
    def situacao(self, media):
        a1.calc_media()
        if media >=7:
            return print("Aprovado")
        elif media >= 5:
            return print("Recuperação")
        else:
            return print("reprovado")

a1 = Aluno("GUstavo", "001", 0)
a1.add_nota(10)
a1.add_nota(7.2)
a1.add_nota(5)
a1.add_nota(4)
m = a1.calc_media()
print(m)
a1.situacao(m)