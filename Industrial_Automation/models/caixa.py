from typing import List
from models.peca import Peca

class Caixa:
    CAPACIDADE_MAXIMA = 10

    def __init__(self, numero: int):
        self.numero = numero
        self.capacidade = self.CAPACIDADE_MAXIMA
        self.pecas: List[Peca] = []
        self.fechada = False

    def adicionar_peca(self, peca: Peca) -> bool:
        if self.fechada:
            return False
        if len(self.pecas) < self.capacidade:
            self.pecas.append(peca)
            if len(self.pecas) == self.capacidade:
                self.fechar()
            return True
        return False

    def fechar(self):
        self.fechada = True

    def esta_cheia(self) -> bool:
        return len(self.pecas) >= self.capacidade

    def __str__(self):
        status = "FECHADA" if self.fechada else "ABERTA"
        return f"Caixa #{self.numero} - {len(self.pecas)}/{self.capacidade} peças - {status}"
