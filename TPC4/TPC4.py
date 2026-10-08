import random

lista = []

continuar = True

while continuar:
    print("\n----- MENU -----" + "\n" * 2 + "(1) Criar Lista\n(2) Ler lista Criar\n(3) Soma\n"
"(4) Média\n(5) Maior\n(6) Menor\n(7) estaOrdenada por ordem crescente\n"
"(8) estaOrdenada por ordem decrescente\n(9) Procura um elemento\n(0) Sair")

    menu = int(input("\nIntroduza o número correspondente à opção desejada: "))

    while menu < 0 or menu > 9:    # enquanto que estiver fora do intervalo volta a pedir um número
        menu = int(input("\nOpção inválida! Introduza o número correspondente à opção desejada: "))

    if menu == 1:
        qt_numeros = int(input("\nQuantos números aleatórios pretende armazenar? "))
    
        i = 1
        lista = []
    
        while i <= qt_numeros:
            num = random.randint(1, 100)
            lista.append(num)
            i = i + 1

        print(f"A lista gerada foi: {lista}")

    elif menu == 2:
        qt_numeros = int(input("\nQuantos números aleatórios pretende armazenar? "))
        
        i = 1
        lista = []
        
        while i <= qt_numeros:
            num = int(input(f"Introduza o {i}º número: "))
            lista.append(num)
            i = i + 1

        print(f"A lista gerada foi: {lista}")

    elif menu == 3:
        if lista == []:
            print("\nA lista está vazia, não tem elementos para somar!")

        else:
            soma = 0
            i = 0

            while i < len(lista):
                soma = soma + lista[i]
                i = i + 1

            print(f"\nA soma dos elementos da lista é: {soma}")

    elif menu == 4:
        if lista == []:
            print("\nA lista está vazia, não tem elementos para fazer uma média!")
        
        else:
            soma = 0
            i = 0
         
            while i < len(lista):
                soma = soma + lista[i]
                i = i + 1

            media = soma / i

            print(f"\nA média dos elementos da lista é: {media: .2f}")

    elif menu == 5:
        if lista == []:
            print("\nA lista está vazia, crie uma primeiro!")
    
        else:
            maior = lista[0]      # assumir que o primeiro da lista é o maior
    
            for elem in lista:    # vai percorrer a lista e se encontrar um número maior que o primeiro ele assume esse valor
                if elem > maior:
                    maior = elem
    
            print(f"\nO maior número da lista é: {maior}")

    elif menu == 6:
        if lista == []:
            print("\nA lista está vazia, crie uma primeiro!")

        else:
            menor = lista[0]      # assumir que o primeiro da lista é o menor

            for elem in lista:    # vai percorrer a lista e se encontrar um número menor que o primeiro ele assume esse valor
                if elem < menor:
                    menor = elem

            print(f"\nO menor número da lista é: {menor}")

    elif menu == 7:
        if lista == []:
            print("\nA lista está vazia, crie uma primeiro!")
        
        else:
            i = 0
            ordenada = True

            while i < len(lista) - 1 and ordenada:
                if lista[i] > lista[i + 1]:
                    ordenada = False

                i = i + 1

            if ordenada == True:
                print("\nA lista está ordenada por ordem crescente.")

            else:
                print("\nA lista não está ordenada por ordem crescente.")

    elif menu == 8:
        if lista == []:
            print("\nA lista está vazia, crie uma primeiro!")
            
        else:
            i = 0
            ordenada = True
    
            while i < len(lista) - 1 and ordenada:
                if lista[i] < lista[i + 1]:
                    ordenada = False
    
                i = i + 1
    
            if ordenada == True:
                print("\nA lista está ordenada por ordem decrescente.")
    
            else:
                print("\nA lista não está ordenada por ordem decrescente.")

    elif menu == 9:

        if lista == []:
            print("\nNão dá para procurar nenhum elemento dado que a lista está vazia!")

        else:
            elem = int(input("\nQue elemento quer procurar na lista? "))

            i = 0
            esta_procura = True

            while i < len(lista) and esta_procura:
                if elem == lista[i]:
                    esta_procura = False
                i = i + 1

            if esta_procura == False:
                print(f"O elemento {elem} está na posição {i - 1} da lista.")

            else:
                i = -1
                print(f"{i}, o elemento não se encontra na lista.")

    elif menu == 0:

        continuar = False

        if lista == []:
            print("\nSaiu do programa, a lista guardada está vazia.")

        else:
            print(f"\nSaiu do programa, a lista guardada foi: {lista}")