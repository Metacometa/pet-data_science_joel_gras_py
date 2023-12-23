from typing import List

Vector = List[float]

def dot(xs: Vector, ys: Vector) -> float:
    assert len(xs) == len(ys), "Векторы должны иметь одинаковую длину"
    return sum(x * y for x, y in zip(xs,  ys))

def sum_of_squares(v: Vector) -> float:
    return dot(v, v)