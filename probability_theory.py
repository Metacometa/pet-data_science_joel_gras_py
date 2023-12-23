from typing import List
import math
import linear_algebra as la
import matplotlib.pyplot as plt

SQRT_TWO_PI = math.sqrt(2 * math.pi)

def normal_pdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (SQRT_TWO_PI * sigma))

def kek():
    xs = [х / 10.0 for х in range(-50, 50)]
    #plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', lаЬеl='мю=О, сигма=l')
    #plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '--', lаЬеl='мю=О, сигма=2')
    #plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], ': ', lаЬеl='мю=О, сигма=О.5')
    #plt.plot(xs, [normal_pdf(x, mu=-1) for x in xs], '-.', lаЬеl='мю=-1, сигма=l')
    plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-.', label='мю=0, сигма=1')
    plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '--', label='мю=0, сигма=2')
    plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], ':', label='мю=0, сигма=0.5')
    plt.plot(xs, [normal_pdf(x, mu=-1) for x in xs], '-.', label='мю=-1, сигма=1')
    plt.legend()
    plt.title("Различные нормальные функции плотности вероятности")
    plt.show()


def expected_value(xs: List[float], ps: List[float]) -> float:
    sum = 0
    for x,p in zip(xs, ps):
        sum += x * p
    return sum

def variance(xs: List[float], ps: List[float]) -> float:
    exptected_val = expected_value(xs, ps)
    squares = [i ** 2 for i in xs]
    return expected_value(squares, ps) - (exptected_val ** 2)

def standart_deviation(xs: List[float], ps: List[float]) -> float:
    return math.sqrt(variance(xs, ps))

def draw(xs: List[float], ps: List[float]):
    plt.plot(xs, ps,marker='o')
    plt.xlabel("x")
    plt.ylabel("p")
    plt.show()

def binominal_distribution(m, n, p):
    q = 1 - p
    combs = math.factorial(n) / (math.factorial(m) * math.factorial(n - m))
    return combs * (p ** m) * (q ** (n - m))

def continious_distribution(f, xs):
    f_x = [f(x) for x in xs]
    plt.plot(xs, f_x)
    plt.show()

def normal(mu, sigma, x):
    return math.exp(-(x - mu) ** 2 / 2 / sigma ** 2) / (SQRT_TWO_PI * sigma)
