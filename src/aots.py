"""
AOTS — Algoritmo de Optimización por Trazas Secuenciales
Implementación de referencia (simulada, clásica)

Demostración conceptual de recuperación por concatenación cuántica.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any


@dataclass
class TraceStep:
    """Un paso de la traza secuencial."""
    index: int
    state_space_size: int
    reduction_factor: float
    candidate: Any = None


@dataclass
class AOTSResult:
    """Resultado de una recuperación AOTS."""
    query: str
    steps: list[TraceStep] = field(default_factory=list)
    final_candidate: Any = None
    complexity_class: str = "O(log n)"

    @property
    def total_reduction(self) -> float:
        if not self.steps:
            return 1.0
        return math.prod(s.reduction_factor for s in self.steps)


class AOTSEngine:
    """
    Motor de recuperación AOTS.

    Simula el colapso progresivo del espacio de estados mediante
    trazas secuenciales concatenadas. En hardware cuántico real,
    cada traza correspondería a una operación de amplitud.
    """

    def __init__(self, corpus: list[Any]):
        self.corpus = corpus
        self.n = len(corpus)

    def recover(self, query: str, steps: int = 3) -> AOTSResult:
        """
        Ejecuta la recuperación.

        Parámetros
        ----------
        query : str
            Consulta de recuperación.
        steps : int
            Número de trazas secuenciales a concatenar.
        """
        result = AOTSResult(query=query)
        space = self.n

        for i in range(steps):
            # Factor de reducción por traza (análogo a amplificación de amplitud)
            reduction = 1.0 / math.sqrt(max(space, 2))
            space = max(int(space * reduction), 1)
            step = TraceStep(
                index=i,
                state_space_size=space,
                reduction_factor=reduction,
            )
            result.steps.append(step)

        # Candidato final: el elemento con mayor similitud a la consulta
        if self.corpus:
            result.final_candidate = max(
                self.corpus,
                key=lambda doc: self._similarity(query, str(doc)),
            )

        return result

    @staticmethod
    def _similarity(query: str, doc: str) -> float:
        q_tokens = set(query.lower().split())
        d_tokens = set(doc.lower().split())
        if not q_tokens or not d_tokens:
            return 0.0
        return len(q_tokens & d_tokens) / len(q_tokens | d_tokens)


def demo() -> None:
    corpus = [
        "Recuperación de información cuántica",
        "Algoritmo de Grover búsqueda",
        "Concatenación de trazas secuenciales",
        "Optimización por superposición",
        "Precedente histórico AOTS",
    ]
    engine = AOTSEngine(corpus)
    result = engine.recover("recuperación cuántica precedente")
    print(f"Consulta: {result.query}")
    print(f"Complejidad: {result.complexity_class}")
    print(f"Reducción total: {result.total_reduction:.4f}")
    print(f"Candidato final: {result.final_candidate}")
    for s in result.steps:
        print(f"  Traza {s.index}: espacio={s.state_space_size}, reducción={s.reduction_factor:.4f}")


if __name__ == "__main__":
    demo()
