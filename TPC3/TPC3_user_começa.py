import random

soma = 0
numVencedor = 1

# números vencedores = 1 + 11 + 11 + 11... (1, 12, 23...)

print(f"""Vamos, alternadamente, somar números de 1 a 10 e quem chegar exatamente aos 100 vence!
Começas tu.""")

while soma < 100:
    num = int(input("Quanto adicionas? "))
    while num < 1 or num > 10:
        num = int(input("O número deve estar entre 1 e 10. Quanto adicionas? "))

    soma = soma + num

# este while só vai aumentar o valor do número vencedor quando a soma for superior a esse valor
# ou seja, se soma for 3, o número vencedor que era 1 passa para 12 e só muda quando a soma for maior que 12
    while numVencedor <= soma:
        numVencedor = numVencedor + 11
    
    print(f"Soma: {soma}")

    if soma == 100:
        print("Ganhaste!")

    elif soma >= 90:
        resto = 100 - soma
        soma = soma + resto
        print(f"""Adiciono {resto}
 Soma: {soma}, Ganhei!""")

# quando a soma for menor que um dos números vencedores e a diferença entre estes for menor que 11 o computador
# vai adicionar essa diferença e a partir daí o computador já tem o jogo controlado

# exemplo: 1 faz com que o número vencedor seja menor ou igual à soma: 1, 
# logo o próximo número vencedor seria 12, mas a diferença é 11 e só podemos jogar de 1 a 10
# então passa para o "else:"

# já o 2 é menor que o número vencedor 12 e a diferença é 10, então o computador pode jogar 10
# e aqui já tem o jogo garantido

    elif soma <= numVencedor and numVencedor - soma < 11:
        numpc = numVencedor - soma
        soma = soma + numpc
        print(f"""Adiciono {numpc}
 Soma: {soma}""")

# neste ponto o computador ainda não tem controlo do jogo, então joga um número aleatório dentro do intervalo
    else:
        numpc = random.randint(1,10)
        soma = soma + numpc
        print(f"""Adiciono {numpc}
 Soma: {soma}""")
    