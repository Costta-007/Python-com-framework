# # Abre o arquivo para escrita (cria/substitui)
# arquivo = open("dados.txt", "w")
# arquivo.write("Linha 1\n")
# arquivo.write("Linha 2\n")
# arquivo.close()


# x  = open('arquivo.txt','w')
# x.write('fhsjkdfhjksdhfjkshdjkfhjsdhfjshdfjkhsjdfksd\n')
# x.close()


# x = open('arquivo.txt', 'a')
# x.write('adiocione....')
# x.close()


# # 1
# arquivo = open('cadastro.csv', 'r')
# for linha in arquivo:
#     dados = linha.strip().split(',')
#     nome =  dados[0]
#     idade = dados[1]
#     venda = dados[2]
#     print('Nome', nome, 'idade', idade, 'vendas', venda)


# arquivo.close()


# # 2
# with open('cadastro.csv', 'r') as c:
#     conteudo = c.read()
#     print(conteudo)


# 3. **Contar linhas**

# Crie uma função `contar_linhas(nome_arquivo)` que retorna o número de linhas do arquivo. Teste com o arquivo `cadastro.txt`.
# arquivo = open("cadastro.txt", "r")
# p = arquivo.readlines()
# print(len(p))

#4. **Procurar palavra**
    
#Peça ao usuário uma palavra e um nome de arquivo. Conte quantas vezes essa palavra aparece no arquivo (ignorando maiúsculas/minúsculas). Exiba o resultado.

# palavra = input("Palavra: ")
# narquivo = input("Arquivo: ")
# arquivo = open(f"{narquivo}.txt", "r")
# p = arquivo.read()
# c = p.count(palavra)
# print(f"Existem {c} palavras em {narquivo}.txt")

#5. **Copiar arquivo**
    
# Peça ao usuário o nome de um arquivo de origem e um arquivo de destino. 
# Copie o conteúdo do arquivo de origem para o destino, mantendo as linhas.

# o = input("Origem: ")
# d = input("Destino: ")

# arquivo_o = open(f"{o}.txt", "r")
# cont = arquivo_o.read()
# arquivo_o.close()
# with open(f"{d}.txt", "w") as arquivo_d:
#     arquivo_d.write(cont)

