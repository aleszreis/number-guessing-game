import random

fim_de_jogo = False

def gerar_numero():
    random_number = random.randint(0, 1000)
    digits = len(str(random_number))

    print(random_number)

    print(f"O número escolhido tem {digits} dígito.") if digits < 2 else print(f"O número escolhido tem {digits} dígitos.")

    return random_number

def checar_resposta(numero):
    global chances

    try:
        resposta = int(input("Dê o seu palpite: "))
    
    except ValueError:
        print(">> O palpite deve ser um número inteiro!\n")

    else:
        if resposta > numero:
            print("Muito alto! Tente um número menor.")
            chances -= 1
            return False

        elif resposta < numero:
            print("Muito baixo! Tente um número maior.")
            chances -= 1
            return False

        else:
            print(f"Acertou!! O número escolhido era o {numero}.\n")
            retry = input("Gostaria de jogar novamente? S/N\n")
            if retry.lower() == "s":
                chances = 15
                numero = gerar_numero()
                return False
            return True


print("Boas vindas ao Guess-a-number!")
print("Foi aleatoriamente gerado um número entre 0 e 1000.\n Você terá 15 chances para acertá-lo e vencer!")

chances = 15
numero = gerar_numero()

while not fim_de_jogo:
    fim_de_jogo = checar_resposta(numero)
    print(f"\n>> Você tem {chances} palpites.\n")

    if chances == 0:
        fim_de_jogo = True
        retry = input("Que pena, acabaram suas chances 😥 Gostaria de tentar novamente? S/N\n")

        if retry.lower() == "s":
            chances = 15
            fim_de_jogo = False
            numero = gerar_numero()
