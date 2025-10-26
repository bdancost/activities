import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu():
    print("\n" + "="*60)
    print("SISTEMA DE GESTÃO DE PEÇAS INDUSTRIAL")
    print("="*60)
    print("1. Cadastrar nova peça")
    print("2. Listar peças aprovadas")
    print("3. Listar peças reprovadas")
    print("4. Remover peça cadastrada")
    print("5. Listar caixas fechadas")
    print("6. Gerar relatório final")
    print("0. Sair do sistema")
    print("="*60)
