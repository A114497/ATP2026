import random
n = random.randint(1, 100)
print("Pensei num número entre 1 e 100. Tenta adivinhar!")
guess = 0
while guess != n:
    guess = int(input("Que número achas que é? "))
    if guess < n:
        print("O número é maior.")
    elif guess > n:
        print("O número é menor.")
print("Adivinhaste o número!")