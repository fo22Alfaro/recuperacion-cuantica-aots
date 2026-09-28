# Precedente Histórico: Recuperación por Concatenación Cuántica

## Contexto

La idea de aplicar principios cuánticos a la recuperación de información no es nueva.
Este documento traza el precedente histórico del enfoque AOTS.

## Línea temporal (conceptual)

1. **Búsqueda clásica** — Complejidad lineal O(n). Cada consulta recorre el espacio completo.
2. **Índices invertidos** — Reducción práctica, pero sigue siendo búsqueda por coincidencia.
3. **Superposición cuántica** — Representación de múltiples candidatos en un solo estado.
4. **Concatenación de trazas** — AOTS: encadenar trazas secuenciales para colapsar el espacio de búsqueda.

## Principio de AOTS

En lugar de buscar elemento por elemento, AOTS construye una **traza concatenada** donde cada paso reduce el espacio de estados de forma exponencial, análogo al algoritmo de Grover pero aplicado a recuperación de documentos y datos estructurados.

## Nota metodológica

Esta es una demostración conceptual. La implementación en hardware cuántico real requiere corrección de errores que aún no está disponible a escala comercial.

## Referencias

- Grover, L. K. (1997). Quantum mechanics helps in searching for a needle in a haystack.
- Brassard, G. et al. (2002). Quantum amplitude amplification and estimation.
