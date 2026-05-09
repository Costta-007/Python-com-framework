
# class Livro:
#     def __init__(self, titulo, autor, ano):
#         self.titulo =  titulo
#         self.autor = autor
#         self.ano = ano
#         self.dispo = True

#     def emprestrar(self):
#       nome  = input('nome: ')
#     #   print(self.dispo)
#       emprestar =  input('Emprestar? ')
#       if emprestar == 'sim':
#         if nome  == self.titulo:
#             if self.dispo == True:
#                 print(self.dispo)
#                 print('esta disponivel ...')
#                 self.dispo = False
#                 print('Emprestado')
#                 return self.dispo

#             else:
#                 print('Não esta diponivel')
#         else:
#             print('Não temos esse livro...')
#     def devolver(self):
#         self.dispo = True
#         print('Livro devolvido')
#         return self.dispo
#     def info(self):
#         return [
#         self.titulo,
#         self.autor,
#         self.ano,
#         self.dispo 
#         ]


# livro =  Livro('Cisne negro', 'taleb','2012')
# livro.emprestrar()
# livro.devolver()
# print(livro.info())


#####################################################

### **2. Classe Funcionário**

# Crie uma classe `Funcionario` com:

# - Atributos: `nome`, `cargo`, `salario_base`
# - Métodos:
#     - `aumentar_salario(percentual)`: aumenta o salário com base no percentual
#     - `calcular_bonus()`: retorna 10% do salário base
#     - `exibir_dados()`: exibe todas as informações
        
#         Crie um funcionário, aumente o salário e mostre os dados atualizados.


# class Funcionario:
#     def __init__(self, nome, cargo, salario_base):
#         self.nome = nome
#         self.cargo = cargo
#         self.salario_base = salario_base
#     def aumentar_salario(self, percentual):
#         self.salario_base += self.salario_base * (percentual / 100)
#         return print(f"o salario agora é {self.salario_base}")
#     def calcular_bonus(self):
#         return self.salario_base * 0.1
#     def exibir_dados(self):
#         return print( [
#             self.nome,
#             self.cargo,
#             self.salario_base,
#         ])
        

# Gustavo = Funcionario("gustavo", "CEO", 10000)
# Gustavo.exibir_dados()
# i = int(input("Aumentar quanto em salario?"))
# Gustavo.aumentar_salario(i)
# Gustavo.calcular_bonus()
# Gustavo.exibir_dados()

######################################################
### **./ Classe Calculadora (estática)**

# Crie uma classe `Calculadora` que **não precisa de atributos**. Apenas métodos de classe (use `@classmethod` ou métodos estáticos) para:

# - `somar(a, b)`
# - `subtrair(a, b)`
# - `multiplicar(a, b)`
# - `dividir(a, b)`
    
#     Teste os métodos sem criar objetos (chamando diretamente pela classe).

#######################################################

### **4. Classe Carro com Controle de Velocidade**

# Crie uma classe `Carro` com:

# - Atributos: `marca`, `modelo`, `velocidade` (inicial 0)
# - Métodos:
#     - `acelerar(valor)`: aumenta a velocidade (não pode ultrapassar 200 km/h)
#     - `frear(valor)`: diminui a velocidade (não pode ficar negativa)
#     - `velocidade_atual()`: exibe a velocidade
        
#         Crie um carro, acelere e freie até parar.


# class Carro:
#     def __init__(self, marca, modelo, velocidade):
#         self.marca = marca
#         self.modelo = modelo
#         self.velocidade = velocidade
#     def acelerar(self,valor):
#         if valor <= 200:
#             self.velocidade += valor
#         else:
#             print("Velocidade muito alta!")
#         return print("VRUUUM")
#     def frear(self, valor):
#         if (self.velocidade - valor) < 0 or (self.velocidade - valor) > 200:
#             print("Paramos!")
#             self.velocidade = 0
#         else:
#             self.velocidade -= valor
#             print(f"Velocidade atual: {self.velocidade}km/h")
#         return print("Freiado!")
#     def velocidade_atual(self):
#         return print(f"Velocidade atual: {self.velocidade}")
    
# c = Carro("Ford", "mustang", 0)

# c.velocidade_atual()
# c.acelerar(201)
# c.velocidade_atual()
# c.acelerar(199)
# c.velocidade_atual()
# c.frear(-10)
# c.velocidade_atual()
# c.acelerar(50)
# c.velocidade_atual()
# c.frear(40)
# c.velocidade_atual()

###############################################
### **4. Classe Agenda**

# Crie uma classe `Agenda` que armazena contatos. Cada contato é um objeto da classe
# `Contato` (crie-a separada), com `nome`, `telefone` e `email`. A classe `Agenda` deve ter:

# - Atributo: `contatos` (lista)
# - Métodos:
#     - `adicionar_contato(contato)`: adiciona à lista
#     - `listar_contatos()`: exibe todos os contatos
#     - `buscar_contato(nome)`: exibe os dados do contato (se existir)
        
#         Crie alguns contatos, adicione-os à agenda e faça buscas.

class Contatos:
    def __init__(self,nome,telefone,email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        


class Agenda:
    def __init__(self, contatos=None):
        self.contatos = contatos =[]
    
    def add_contato(self,contato):
        self.contatos.append(contato)
        return(print("Contato add"))
    
    def listar_contato(self):
        for c in self.contatos:
            print(f"Nome: {c.nome} | Tel: {c.telefone} | Email: {c.email}")
    def buscar_contato(self,nome):
        encontrado = False
        
        for c in self.contatos:
            if c.nome.lower() == nome.lower():
                print("\n--- Contato Encontrado ---")
                print(f"Nome: {c.nome} | Tel: {c.telefone} | Email: {c.email}")
                encontrado = True
                break 
        
        if not encontrado:
            print(f"\nO contato '{nome}' não foi encontrado na agenda.")

 
        

id1 = Contatos("Gustavo",990022,"gugu@gmail.com")
id2 = Contatos("dionatan",9900124122,"gagagagagagu@gmail.com")
agenda = Agenda()

agenda.add_contato(id1)
agenda.add_contato(id2)
agenda.listar_contato()
agenda.buscar_contato("gustavo")