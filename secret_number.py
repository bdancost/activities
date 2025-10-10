# Importa a biblioteca random para gerar números aleatórios
import random

# Gera um número secreto aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

tentativas = 0

print("Bem-vindo ao jogo de adivinhar o número!")
print("Estou pensando em um número entre 1 e 10. Tente adivinhar!")

while True:
    # Pede para o usuário digitar um número
    chute = int(input("Digite seu palpite: "))
    tentativas += 1

    if chute == numero_secreto:
        print(f"🎉 Parabéns! Você acertou em {tentativas} tentativas.")
        break
    elif chute < numero_secreto:
        print("O número é maior! Tente novamente.")
    else:
        print("O número é menor! Tente novamente.")

print("Fim do jogo.")