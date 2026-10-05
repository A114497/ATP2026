soma = 1

print(f"""Vamos, alternadamente, somar números de 1 a 10 e quem chegar exatamente aos 100 vence!
Começo eu, {soma}!""")

while soma < 100:
    num = int(input("Quanto adicionas? "))
    while num < 1 or num > 10:
        num = int(input("O número deve estar entre 1 e 10. Quanto adicionas? "))
    soma = soma + num
    print(f"Soma: {soma}")
    if soma >= 90:
        resto = 100 - soma
        soma = soma + resto
        print(f"""Adiciono {resto}
 Soma: {soma}, Ganhei!""")
    else:
        numpc = 11 - num
        soma = soma + numpc
        print(f"""Adiciono {numpc}
Soma: {soma}""")