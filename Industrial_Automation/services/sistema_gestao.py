from typing import List
from models.peca import Peca
from models.caixa import Caixa

class SistemaGestao:
    def __init__(self):
        self.pecas_aprovadas: List[Peca] = []
        self.pecas_reprovadas: List[Peca] = []
        self.caixas: List[Caixa] = [Caixa(1)]  # Inicia com a primeira caixa
        self.contador_pecas = 0

    def cadastrar_peca(self, peso: float, cor: str, comprimento: float):
        self.contador_pecas += 1
        id_peca = f"P{self.contador_pecas:04d}"
        peca = Peca(id_peca, peso, cor, comprimento)

        if peca.aprovada:
            self.pecas_aprovadas.append(peca)
            self._armazenar_peca(peca)
            print(f"\n✓ Peça {id_peca} cadastrada e APROVADA!")
        else:
            self.pecas_reprovadas.append(peca)
            print(f"\n✗ Peça {id_peca} cadastrada mas REPROVADA!")
            print(f"  Motivo: {peca.motivo_reprovacao}")

    def _armazenar_peca(self, peca: Peca):
        caixa_atual = self.caixas[-1]
        if caixa_atual.esta_cheia():
            nova_caixa = Caixa(len(self.caixas) + 1)
            self.caixas.append(nova_caixa)
            caixa_atual = nova_caixa
            print(f"  → Nova caixa #{caixa_atual.numero} iniciada!")
        caixa_atual.adicionar_peca(peca)
        if caixa_atual.fechada:
            print(f"  → Caixa #{caixa_atual.numero} FECHADA (capacidade máxima atingida)!")

    def listar_pecas_aprovadas(self):
        if not self.pecas_aprovadas:
            print("\nNenhuma peça aprovada cadastrada ainda.")
            return

        print("\n" + "="*60)
        print("PEÇAS APROVADAS")
        print("="*60)
        for peca in self.pecas_aprovadas:
            print(peca)
        print("="*60)

    def listar_pecas_reprovadas(self):
        if not self.pecas_reprovadas:
            print("\nNenhuma peça reprovada cadastrada ainda.")
            return

        print("\n" + "="*60)
        print("PEÇAS REPROVADAS")
        print("="*60)
        for peca in self.pecas_reprovadas:
            print(peca)
        print("="*60)

    def remover_peca(self, id_peca: str):
        # Procura nas peças aprovadas
        for i, peca in enumerate(self.pecas_aprovadas):
            if peca.id == id_peca:
                self.pecas_aprovadas.pop(i)
                print(f"\n✓ Peça {id_peca} removida com sucesso!")
                return

        # Procura nas peças reprovadas
        for i, peca in enumerate(self.pecas_reprovadas):
            if peca.id == id_peca:
                self.pecas_reprovadas.pop(i)
                print(f"\n✓ Peça {id_peca} removida com sucesso!")
                return

        print(f"\n✗ Peça {id_peca} não encontrada!")

    def listar_caixas(self):
        caixas_fechadas = [c for c in self.caixas if c.fechada]

        if not caixas_fechadas:
            print("\nNenhuma caixa fechada ainda.")
            return

        print("\n" + "="*60)
        print("CAIXAS FECHADAS")
        print("="*60)
        for caixa in caixas_fechadas:
            print(caixa)
            print(f"  Peças: {', '.join([p.id for p in caixa.pecas])}")
        print("="*60)

    def gerar_relatorio(self):
        print("\n" + "="*60)
        print("RELATÓRIO FINAL DO SISTEMA")
        print("="*60)

        total_pecas = len(self.pecas_aprovadas) + len(self.pecas_reprovadas)
        print(f"\nTotal de peças processadas: {total_pecas}")
        print(f"  ✓ Aprovadas: {len(self.pecas_aprovadas)}")
        print(f"  ✗ Reprovadas: {len(self.pecas_reprovadas)}")

        if self.pecas_reprovadas:
            print("\nMotivos de reprovação:")
            motivos = {}
            for peca in self.pecas_reprovadas:
                if peca.motivo_reprovacao in motivos:
                    motivos[peca.motivo_reprovacao] += 1
                else:
                    motivos[peca.motivo_reprovacao] = 1
            for motivo, qtd in motivos.items():
                print(f"  • {motivo}: {qtd} peça(s)")

        caixas_fechadas = [c for c in self.caixas if c.fechada]
        caixas_abertas = [c for c in self.caixas if not c.fechada]

        print(f"\nCaixas utilizadas: {len(self.caixas)}")
        print(f"  → Fechadas: {len(caixas_fechadas)}")
        print(f"  → Em uso: {len(caixas_abertas)}")

        if caixas_abertas:
            caixa_atual = caixas_abertas[0]
            print(f"  → Caixa atual: #{caixa_atual.numero} com {len(caixa_atual.pecas)}/10 peças")

        if total_pecas > 0:
            taxa_aprovacao = (len(self.pecas_aprovadas) / total_pecas) * 100
            print(f"\nTaxa de aprovação: {taxa_aprovacao:.1f}%")

        print("="*60)
