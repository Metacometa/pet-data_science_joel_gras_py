from typing import List
import math
import linear_algebra as la

#среднее
def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)

def median(xs: List[float]) -> float:
    n = len(xs)
    sorted_xs = sorted(xs)
    return sorted_xs[n // 2] if (n % 2 == 0) else (sorted_xs[n // 2] + sorted_xs[n // 2 - 1]) / 2

def data_range(xs: List[float]) -> float:
    return max(xs) - min(xs)

def de_mean(xs: List[float]) -> List[float]:
    xs_mean = mean(xs)
    return [x - xs_mean for x in xs]

def variance(xs: List[float]) -> float:
    deviations = de_mean(xs)
    return la.sum_of_squares(deviations) / len(xs)

def standart_deviation(xs: List[float]) -> float:
    return math.sqrt(variance(xs))

def covariance(xs: List[float], ys: List[float]) -> float:
    return la.dot(de_mean(xs), de_mean(ys)) (len(xs) - 1)