perguntas = [
    ["Quanto é 2 + 2?", "4"],
    ["Qual linguagem estamos aprendendo?", "python"],
    ["Qual animal é famoso por rir? (dica: aparece no Rei Leão)", "hiena"],
    ["Qual fruta rima com limão e é amarela?", "mamão"],
    ["Qual o nome do robô do Star Wars que parece um latão?", "r2d2"]
]

acertos = 0

for pergunta in perguntas:
    resposta = input(pergunta[0] + " ")
    if resposta.lower() == pergunta[1]:
        acertos += 1

print(f"Você acertou {acertos} de {len(perguntas)} perguntas!")