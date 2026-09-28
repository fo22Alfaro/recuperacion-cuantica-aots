"""Pruebas de validación para AOTS."""

import math
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from aots import AOTSEngine, TraceStep, AOTSResult


def test_engine_instantiates():
    engine = AOTSEngine(["a", "b", "c"])
    assert engine.n == 3


def test_recover_returns_result():
    engine = AOTSEngine(["doc uno", "doc dos", "doc tres"])
    result = engine.recover("doc")
    assert isinstance(result, AOTSResult)
    assert result.query == "doc"
    assert len(result.steps) == 3


def test_trace_steps_reduce_space():
    engine = AOTSEngine(list(range(1000)))
    result = engine.recover("test", steps=4)
    sizes = [s.state_space_size for s in result.steps]
    assert sizes == sorted(sizes, reverse=True)
    assert sizes[-1] < 1000


def test_complexity_class():
    engine = AOTSEngine(["x"])
    result = engine.recover("x")
    assert result.complexity_class == "O(log n)"


def test_similarity_identical():
    from aots import AOTSEngine
    s = AOTSEngine._similarity("hola mundo", "hola mundo")
    assert math.isclose(s, 1.0)


def test_similarity_disjoint():
    from aots import AOTSEngine
    s = AOTSEngine._similarity("hola", "adios")
    assert s == 0.0


if __name__ == "__main__":
    test_engine_instantiates()
    test_recover_returns_result()
    test_trace_steps_reduce_space()
    test_complexity_class()
    test_similarity_identical()
    test_similarity_disjoint()
    print("Todas las pruebas pasaron.")
