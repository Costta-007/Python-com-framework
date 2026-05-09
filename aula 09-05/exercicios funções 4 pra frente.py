#### *3. Gerador de Tabuada*

#Escreva uma função tabuada(numero, inicio=1, fim=10) que exibe a tabuada do numero no intervalo [inicio, fim].
#Se os argumentos inicio e fim não forem fornecidos, use 1 e 10.

#def tabuada(n, ini = 1, fim = 10):
#    for x in range(ini,fim+1):
#        print(f"{n} x {x} = {n * x}")
#tabuada(17,5,890890)
#++++++++++++++++++++++===================++++++++++++++++++++++++++++++++
### *4. Contador de Palavras*

#Crie uma função contar_palavras(texto) que retorna um dicionário com a contagem de cada palavra no texto
#(considere palavras separadas por espaços). O programa principal deve ler uma frase e exibir o resultado.

#texto = input("Digite o texto: ")
#def contar_palavras(txt):
#    palavras = txt.split()
#    totalP = len(palavras)
#    return totalP
#print(f"Total de palavras: {contar_palavras(texto)}")
#++++++++++++++++++++++===================++++++++++++++++++++++++++++++++
### *5. Ordenação Personalizada*

#Implemente uma função ordenar_lista(lista, crescente=True) que retorna### *5. Ordenação Personalizada*

#Implemente uma função ordenar_lista(lista, crescente=True) que retorna uma nova lista ordenada. Se crescente=True, ordena em ordem crescente; caso contrário, decrescente. Não use sorted() ou list.sort() (implemente o algoritmo de ordenação de sua escolha, como bolha). uma nova lista ordenada.
#Se crescente=True, ordena em ordem crescente; caso contrário, decrescente. Não use sorted() ou list.sort() (implemente o algoritmo de ordenação de sua escolha, como bolha).

#lista = [1,24,3,46,2,6,7,89,4,232,654,8,4563,346,7]
#def ordernar_lista(lista , crescente = True):
#    tamanhoL = len(lista)
#    print(tamanhoL)
#    print(range(tamanhoL))
#    for i in range(tamanhoL):
#        for x in range(tamanhoL - 1):
#            if crescente:
#                if lista[x] > lista[x+1]: 
#                    lista[x],lista[x+1] = lista[x+1] , lista[x]
#            else:
#                if lista[x] < lista[x+1]: 
#                    lista[x],lista[x+1] = lista[x+1] , lista[x]
#            
#            
#    return lista

#print(ordernar_lista(lista,False))

#++++++++++++++++++++++===================++++++++++++++++++++++++++++++++

### *6. Jogo de Adivinhação*

#Crie uma função jogar() que sorteia um número entre 1 e 100 e dá dicas ("maior", "menor") até o usuário acertar.
#Use random.randint(). A função deve retornar o número de tentativas. No programa principal, chame a função e exiba quantas tentativas foram necessárias.

import random as rand

def jogar():
    tent = 2
    r = 1
    n = rand.randint(1,100)
    print("Olá, eu sou o gênio dos números! Eu pensei em um numero entre 1 e 100,\nvocê consegue adivinhar ou é só um fracote??\n")
    print(n)
    while tent >=0:
        try:
            t = int(input())
            if (t == n):
                print(f"Você adivinhou! Que improvável!\n(tentativas = {r}) (Numero: {n})")
                print(tent)
                op = input("\nJogar novamente?(s/n): ")
                if op == "s":
                    print("\nNovamente? Agora você perde!")
                    r = 0
                    tent =2
                else:
                    quit()
            elif tent ==0:
                print("\nQue peninha, você perdeu :( ... Haha, já esperava isso.")
                op = input("Jogar novamente?(s/n): ")
                if op == "s":
                    print("\nUm filosofo disse que é loucura repetir o mesmo erro\nesperando outros resultados. Acredito que você seja o louco.")
                    r = 0
                    tent = 2
                else:
                    quit()
            else :
                if t < n and tent >0:
                    print(f"Você errou, tem {tent} tentativas, o numero que escolhi é maior\n")
                 
                elif t > n and tent > 0:
                    print(f"Você errou, tem {tent} tentativa(s), o numero que escolhi é menor\n")
                r +=1   
                tent -=1
        except ValueError:
            print("Escolha um numero válido!")


def main():
    print("""       Genio do numero!        
            [1] Jogar
            [2] Sair        """)
    while True:
        try:
            i = int(input())
            if i == 1:
                jogar()
                break
            elif i == 2:
                quit()
            else:
                print("Selecione opção válida!")
        except ValueError:
            print("Selecione opçção válida!")
main()