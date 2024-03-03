# Jogo da adivinhação

from random import randint

print("\n")
print("*" * 30)
print("\nSeja bem vindo ao jogo de adivinhação!\n")
print("Neste jogo você deverá descobrir um número secreto, boa sorte!\n")
print("*" * 30)
print("\n")


def iniciar_jogo():
    while True:
        dificuldade = int(input("\nPrimeiro escolha o nível de dificuldade: 1 - fácil, 2 - médio, 3 - difícil\n"))
        if dificuldade == 1:
            print("\nVocê escolheu a dificuldade fácil!\n\nIniciando jogo, boa sorte!\n")
            maximo = 5
            break
        elif dificuldade == 2:
            print("\nVocê escolheu a dificuldade média!\n\nIniciando jogo, boa sorte!\n")
            maximo = 10
            break
        elif dificuldade == 3:
            print("\nVocê escolheu a dificuldade difícil!\n\nIniciado jogo, boa sorte!\n")
            maximo = 15
            break
        else:
            print("\nO grau de dificuldade deve ser de 1 a 3.")
    
    numero_secreto = randint(1, maximo)
    numero_escolhido = 0

    while True:
        try:
            numero_escolhido = int(input(f"Escolha um número de 1 a {maximo}: "))
        except:
            print("Você escolheu um número inválido!")
        else:
            if numero_escolhido > maximo:
                print(f"Número precisa estar entre 1 e {maximo}!")
            elif numero_escolhido == numero_secreto:
                print(f"\n\nParabéns!\nVocê acertou o número secreto é {numero_secreto}! \n")
                jogar_novamente = input("\nDeseja jogar novamente? (S - Sim, N - Não)\n")
                if jogar_novamente.lower() == "s":
                    iniciar_jogo()
                else:
                    print("Jogo encerrado!\n")
                    quit()
            else:
                print("Você errou, tente novamente!\n")

while True:
    opcao = input("Deseja iniciar o jogo? (S - Sim / N - Não): \n")
    if opcao.lower() == "s":
        iniciar_jogo()
        
    elif opcao.lower() == "n":
        print("\n\nJogo encerrado!\n")
        break
    else:
        print("Digito inválido, tente novamente!\n")