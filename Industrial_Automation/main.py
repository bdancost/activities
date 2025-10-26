from services.sistema_gestao import SistemaGestao
from utils.helpers import limpar_tela, exibir_menu

def main():
    sistema = SistemaGestao()

    print("\n" + "="*60)
    print("BEM-VINDO AO SISTEMA DE GESTÃO DE PEÇAS")
    print("="*60)
    print("\nCritérios de Qualidade:")
    print("  • Peso: entre 95g e 105g")
    print("  • Cor: azul ou verde")
    print("  • Comprimento: entre 10cm e 20cm")
    print("  • Capacidade por caixa: 10 peças")

    while True:
        exibir_menu()
        try:
            opcao = input("\nEscolha uma opção: ").strip()

            if opcao == "1":
                print("\n--- CADASTRO DE NOVA PEÇA ---")
                peso = float(input("Peso (gramas): "))
                cor = input("Cor: ").strip()
                comprimento = float(input("Comprimento (cm): "))
                sistema.cadastrar_peca(peso, cor, comprimento)
                input("\nPressione ENTER para continuar...")

            elif opcao == "2":
                sistema.listar_pecas_aprovadas()
                input("\nPressione ENTER para continuar...")

            elif opcao == "3":
                sistema.listar_pecas_reprovadas()
                input("\nPressione ENTER para continuar...")

            elif opcao == "4":
                id_peca = input("\nDigite o ID da peça a remover (ex: P0001): ").strip().upper()
                sistema.remover_peca(id_peca)
                input("\nPressione ENTER para continuar...")

            elif opcao == "5":
                sistema.listar_caixas()
                input("\nPressione ENTER para continuar...")

            elif opcao == "6":
                sistema.gerar_relatorio()
                input("\nPressione ENTER para continuar...")

            elif opcao == "0":
                print("\n✓ Encerrando o sistema...")
                print("Obrigado por utilizar o Sistema de Gestão de Peças!")
                break

            else:
                print("\n✗ Opção inválida! Tente novamente.")
                input("\nPressione ENTER para continuar...")

        except ValueError:
            print("\n✗ Erro: Digite um valor numérico válido!")
            input("\nPressione ENTER para continuar...")
        except KeyboardInterrupt:
            print("\n\n✓ Sistema interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"\n✗ Erro inesperado: {e}")
            input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    main()
