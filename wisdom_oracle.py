print('Sou o Oráculo da Sabedoria Python. Faça sua pergunta...')

pergunta = input('Você quer saber sobre (funções, loops, variáveis, listas)? ')

match pergunta:
    case 'funções' | 'funcoes' | 'funcao':
        print('Funções são blocos de código que você pode reutilizar! def nome():')
    case 'loops':
        print('Loops permitem repetir ações. Use for ou while!')
    case 'variáveis':
        print('Variáveis guardam valores. Exemplo: idade = 18')
    case 'listas':
        print('Listas guardam vários valores. Ex: frutas = ["maçã", "banana"]')
    case _:
        print('Essa resposta está além do meu conhecimento atual.')