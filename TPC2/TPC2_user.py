liminf = 1
limsup = 100
resposta = "não"
print(f"Pense num número entre {liminf} e {limsup}")
while resposta != "sim":
    numero = (liminf + limsup) // 2
    resposta = input(f"O teu número é {numero}? ")
    if resposta == "não":
        dif = input(f"É maior ou menor que {numero}? ")
        if dif == "maior":
            liminf = numero + 1
        elif dif == "menor":
            limsup = numero - 1
print(f"Adivinhei o teu número!")
