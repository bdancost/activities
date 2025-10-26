from typing import List

class Peca:
    def __init__(self, id: str, peso: float, cor: str, comprimento: float):
        self.id = id
        self.peso = peso
        self.cor = cor.lower()
        self.comprimento = comprimento
        self.aprovada = False
        self.motivo_reprovacao = ""
        self._validar_qualidade()

    def _validar_qualidade(self):
        motivos = []

        if not (95 <= self.peso <= 105):
            motivos.append(f"Peso fora do padrão ({self.peso}g)")
        if self.cor not in ['azul', 'verde']:
            motivos.append(f"Cor inválida ({self.cor})")
        if not (10 <= self.comprimento <= 20):
            motivos.append(f"Comprimento fora do padrão ({self.comprimento}cm)")

        if not motivos:
            self.aprovada = True
        else:
            self.motivo_reprovacao = ", ".join(motivos)

    def __str__(self):
        status = "✓ APROVADA" if self.aprovada else "✗ REPROVADA"
        info = f"ID: {self.id} | Peso: {self.peso}g | Cor: {self.cor} | Comprimento: {self.comprimento}cm | {status}"
        if not self.aprovada:
            info += f"\n  Motivo: {self.motivo_reprovacao}"
        return info
